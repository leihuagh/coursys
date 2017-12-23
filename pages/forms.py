from django import forms
from django.db import transaction
from pages.models import Page, PageVersion, READ_ACL_CHOICES, WRITE_ACL_CHOICES
from importer import HTMLWiki
from courselib.markup import MarkupContentField
import urllib2, urlparse


class WikiField(forms.CharField):
    # TODO: search and destroy other usages
    def __init__(self, *args, **kwargs):
        self.widget = forms.Textarea(attrs={'cols': 70, 'rows': 20})
        if 'help_text' not in kwargs:
            kwargs['help_text'] = 'Page formatted in <a href="/docs/pages">WikiCreole markup</a>.' # hard-coded URL since this is evaluated before urls.py: could be reverse_lazy?
        super(WikiField, self).__init__(*args, **kwargs)

class CommentField(forms.CharField):
    def __init__(self, *args, **kwargs):
        self.widget = forms.TextInput(attrs={'size': 60})
        if 'required' not in kwargs:
            kwargs['required'] = False
        if 'help_text' not in kwargs:
            kwargs['help_text'] = 'Comment on this change'
        super(CommentField, self).__init__(*args, **kwargs)


class EditPageFileForm(forms.ModelForm):
    releasedate = forms.DateField(initial=None, required=False, label="Release Date",
                help_text='Date the "can read" permissions take effect. Leave blank for no timed-release. Pages can always be viewed by instructors and TAs.')
    # disabling editing-release UI on the basis that probably nobody needs it
    #editdate = forms.DateField(initial=None, required=False, label="Editable Date",
    #            help_text='Date the "can change" permissions take effect. Leave blank for no timed-release. Pages can always be edited by instructors and TAs.')
    def __init__(self, offering, *args, **kwargs):
        super(EditPageFileForm, self).__init__(*args, **kwargs)
        # force the right course offering into place
        self.offering = offering
        self.fields['offering'].initial = offering.id
        
        # existing data for other fields
        if self.instance.id:
            version = self.instance.current_version()
            self.initial['title'] = version.title
            self.initial['markup_content'] = [version.wikitext, version.markup(), version.math()]
            self.initial['releasedate'] = self.instance.releasedate()
            self.initial['editdate'] = self.instance.editdate()
        
        # tidy up ACL choices: remove NONE
        self.fields['can_read'].choices = [(v,l) for (v,l) in self.fields['can_read'].choices
                                           if v != 'NONE']
        self.fields['can_write'].choices = [(v,l) for (v,l) in self.fields['can_write'].choices
                                           if v != 'NONE']


    def clean_offering(self):
        if self.cleaned_data['offering'] != self.offering:
            raise forms.ValidationError("Wrong course offering.")
        return self.cleaned_data['offering']

    @transaction.atomic
    def clean_label(self):
        label = self.cleaned_data['label']
        error = self.instance.label_okay(label)
        if error:
            raise forms.ValidationError(error)
        return label

    class Meta:
        model = Page
        exclude = ('config',)
        widgets = {
            'offering': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'size':50}),
            'label': forms.TextInput(attrs={'size':20}),
        }


class EditPageForm(EditPageFileForm):
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'size':50}))
    markup_content = MarkupContentField(label='Content', with_wysiwyg=True)
    comment = CommentField()

    @transaction.atomic
    def save(self, editor, *args, **kwargs):
        # also create the PageVersion object.
        wikitext, markup, math = self.cleaned_data['markup_content']
        comment = self.cleaned_data['comment']
        title = self.cleaned_data['title']
        pv = PageVersion(title=title, wikitext=wikitext, comment=comment, editor=editor)
        # set config data
        pv.set_markup(markup)
        pv.set_math(math)

        self.instance.offering = self.offering
        pg = super(EditPageForm, self).save(*args, **kwargs)
        pv.page=self.instance
        pv.save()
        return pg


class EditPageFormRestricted(EditPageForm):
    """
    Restricted version of EditPageForm for students.
    """
    def __init__(self, *args, **kwargs):
        super(EditPageFormRestricted, self).__init__(*args, **kwargs)
        if self.instance.label:
            # can't change label, but can set for a new page
            del self.fields['label']
        del self.fields['can_write']
        if 'releasedate' in self.fields:
            del self.fields['releasedate']
        if 'editdate' in self.fields:
            del self.fields['editdate']

EditPageForm.restricted_form = EditPageFormRestricted


class EditFileForm(EditPageFileForm):
    file_attachment = forms.FileField(label="File")

    @transaction.atomic
    def save(self, editor, *args, **kwargs):
        # also create the PageVersion object.
        upfile = self.cleaned_data['file_attachment']
        pv = PageVersion(file_attachment=upfile, file_mediatype=upfile.content_type,
                         file_name=upfile.name, editor=editor)

        self.instance.offering = self.offering
        pg = super(EditFileForm, self).save(*args, **kwargs)
        pv.page=self.instance
        pv.save()
        return pg

class EditFileFormRestricted(EditFileForm):
    """
    Restricted version of EditFileForm for students.
    """
    def __init__(self, *args, **kwargs):
        super(EditFileFormRestricted, self).__init__(*args, **kwargs)
        if self.instance.label:
            # can't change label, but can set for a new page
            del self.fields['label']
        del self.fields['can_write']

EditFileForm.restricted_form = EditFileFormRestricted


class PageImportForm(forms.Form):
    file = forms.FileField(required=False)
    url = forms.URLField(required=False, label='URL', widget=forms.TextInput(attrs={'size':70}))
    
    def clean(self):
        url = self.cleaned_data.get('url', None)
        file = self.cleaned_data.get('file', None)
        
        if not url and not file:
            raise forms.ValidationError("Must provide either an HTML file or URL.")
        elif url and file:
            raise forms.ValidationError("Can only provide one of the file and URL.")
        
        return self.cleaned_data

    def _html_to_wiki(self, html):
        converter = HTMLWiki([])
        try:
            wiki = converter.from_html(html)
        except converter.ParseError:
            raise forms.ValidationError("Could not parse the HTML file.")

        return wiki

    
    def clean_url(self):
        url = self.cleaned_data['url']
        if not url:
            return None
        
        try:
            fh = urllib2.urlopen(url, timeout=20)
            html = fh.read()
        except:
            raise forms.ValidationError("Could not fetch the URL.")

        return self._html_to_wiki(html)

    def clean_file(self):
        file = self.cleaned_data['file']
        if file is None:
            return None

        if file.content_type not in ['text/html', 'application/xhtml+xml']:
            raise forms.ValidationError("Only HTML/XHTML files can be imported")

        html = file.read()
        return self._html_to_wiki(html)

