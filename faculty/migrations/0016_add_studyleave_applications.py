# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-01 14:15
from __future__ import unicode_literals

import autoslug.fields
import courselib.json_fields
from django.db import migrations, models
import django.db.models.deletion
import faculty.event_types.awards
import faculty.event_types.career
import faculty.event_types.info
import faculty.event_types.position
import faculty.event_types.teaching


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0015_add_letter_option_to_memos'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyLeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(blank=True, choices=[(b'LLEC', b'Limited-Term Lecturer'), (b'LABI', b'Laboratory Instructor'), (b'LECT', b'Lecturer'), (b'SLEC', b'Senior Lecturer'), (b'INST', b'Instructor'), (b'ASSI', b'Assistant Professor'), (b'ASSO', b'Associate Professor'), (b'FULL', b'Full Professor'), (b'URAS', b'University Research Associate'), (b'ADJC', b'Adjunct Professor')], max_length=4, null=True)),
                ('tenure', models.CharField(choices=[(b'YES', b'Yes'), (b'INPR', b'Tenure Application In Process'), (b'NO', b'No')], default=b'NO', max_length=4)),
                ('tenure_date', models.DateField(blank=True, null=True, verbose_name=b'if yes, date awarded')),
                ('start_date', models.DateField(blank=True, help_text=b'Start date requested', null=True)),
                ('end_date', models.DateField(blank=True, help_text=b'End date requested', null=True)),
                ('leave_option', models.CharField(blank=True, choices=[(b'A', b'A - 3 consecutive semesters at 80% after 6 years of service'), (b'B', b'B - 2 consecutive semesters at 90% after 6 years of service'), (b'C', b'C - 1 consecutive semester at 100% after 6 years of service'), (b'D', b'D - 2 consecutive semesters at 80% after 4 years of service'), (b'E', b'E - 1 consecutive semester at 90% after 3 years of service')], max_length=1, null=True)),
                ('defer_salary', models.BooleanField(choices=[(True, b'Yes'), (False, b'No')], default=False, help_text=b'The faculty member may choose to defer part of salary prior to the study leave in order to spread the impact of the salary reduction. When the faculty member chooses this feature, the salary will be reduced following the approval of the study leave by the Vice President, Academic. The salary deferral arrangements must be completed by the end of the study leave. Salary deferral may be exercised only for a leave which exceeds six months. /nExample: A study leave Option A - 80% for 12 months, is approved in December 2017 with the study leave schedule to start on September 1, 2019. This would result in a salary at the level of 88% over the 20 month period from January 1, 2018 to August 31, 2019.')),
                ('first_study_leave', models.CharField(choices=[(b'YES', b'Yes'), (b'NO', b'No'), (b'NA', b'N/A')], default=None, max_length=3, verbose_name=b'Is this your first study leave after being granted tenure')),
                ('appointed_tenure', models.CharField(choices=[(b'YES', b'Yes'), (b'NO', b'No'), (b'NA', b'N/A')], default=None, max_length=3, verbose_name=b'Were you appointed with tenure')),
                ('first_study_leave_after_6_years', models.CharField(choices=[(b'YES', b'Yes'), (b'NO', b'No'), (b'NA', b'N/A')], default=None, max_length=3, verbose_name=b'Continuing Teaching Faculty, Continuing Librarians/Archivist, is this your first study leave after six years service')),
                ('service_credits', models.CharField(blank=True, max_length=400, null=True, verbose_name=b'List all academic service credits from other similar institutions (for first study leave only)')),
                ('leave_1_start_date', models.DateField(blank=True, help_text=b'List all previous study leaves since first continuing appointment.', null=True, verbose_name=b'1st leave start date')),
                ('leave_1_end_date', models.DateField(blank=True, null=True, verbose_name=b'1st leave end date')),
                ('leave_2_start_date', models.DateField(blank=True, null=True, verbose_name=b'2nd leave start date')),
                ('leave_2_end_date', models.DateField(blank=True, null=True, verbose_name=b'2nd leave end date')),
                ('leave_3_start_date', models.DateField(blank=True, null=True, verbose_name=b'3rd leave start date')),
                ('leave_3_end_date', models.DateField(blank=True, null=True, verbose_name=b'3rd leave end date')),
                ('leave_4_start_date', models.DateField(blank=True, null=True, verbose_name=b'4th leave start date')),
                ('leave_4_end_date', models.DateField(blank=True, null=True, verbose_name=b'4th leave end date')),
                ('leave_5_start_date', models.DateField(blank=True, null=True, verbose_name=b'5th leave start date')),
                ('leave_5_end_date', models.DateField(blank=True, null=True, verbose_name=b'5th leave end date')),
                ('leave_6_start_date', models.DateField(blank=True, null=True, verbose_name=b'6th leave start date')),
                ('leave_6_end_date', models.DateField(blank=True, null=True, verbose_name=b'6th leave end date')),
                ('grad_students', models.BooleanField(choices=[(True, b'Yes'), (False, b'No')], default=False, verbose_name=b'Do you supervise Graduate Students')),
                ('masters_students', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Number of Masters Students')),
                ('phd_students', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Number of PhD/EdD Students')),
                ('manage_students_during_leave', models.CharField(blank=True, max_length=400, null=True, verbose_name=b'If you plan to manage Graduate Students during the study leave period, please provide details')),
                ('hidden', models.BooleanField(default=False, editable=False)),
                ('config', courselib.json_fields.JSONField(blank=True, default={}, editable=False, null=True)),
                ('last_modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'autoslug', unique=True)),
                ('last_modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='coredata.Person')),
                ('person', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='coredata.Person')),
                ('primary_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studyleaveapplications', to='coredata.Unit')),
                ('secondary_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='coredata.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='StudyLeaveSemesterActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(choices=[(b'ADMN', b'Admin Leave'), (b'MEDC', b'Medical Leave'), (b'OTHR', b'Other'), (b'PARN', b'Parent Leave'), (b'RESC', b'Research'), (b'STUD', b'Study Leave'), (b'TEAC', b'Teaching')], max_length=4)),
                ('hidden', models.BooleanField(default=False, editable=False)),
                ('config', courselib.json_fields.JSONField(blank=True, default={}, editable=False, null=True)),
                ('last_modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'autoslug', unique=True)),
                ('application', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='faculty.StudyLeaveApplication')),
                ('last_modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='coredata.Person')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coredata.Semester')),
            ],
        ),
        migrations.AlterField(
            model_name='careerevent',
            name='event_type',
            field=models.CharField(choices=[(b'ADMINPOS', faculty.event_types.position.AdminPositionEventHandler), (b'APPOINT', faculty.event_types.career.AppointmentEventHandler), (b'AWARD', faculty.event_types.awards.AwardEventHandler), (b'COMMITTEE', faculty.event_types.info.CommitteeMemberHandler), (b'EXTERN_AFF', faculty.event_types.info.ExternalAffiliationHandler), (b'EXTSERVICE', faculty.event_types.info.ExternalServiceHandler), (b'FELLOW', faculty.event_types.awards.FellowshipEventHandler), (b'GRANTAPP', faculty.event_types.awards.GrantApplicationEventHandler), (b'NORM_TEACH', faculty.event_types.teaching.NormalTeachingLoadHandler), (b'LEAVE', faculty.event_types.career.OnLeaveEventHandler), (b'ONE_NINE', faculty.event_types.teaching.OneInNineHandler), (b'OTHER_NOTE', faculty.event_types.info.OtherEventHandler), (b'LABMEMB', faculty.event_types.info.ResearchMembershipHandler), (b'SALARY', faculty.event_types.career.SalaryBaseEventHandler), (b'STIPEND', faculty.event_types.career.SalaryModificationEventHandler), (b'SPCL_DEAL', faculty.event_types.info.SpecialDealHandler), (b'STUDYLEAVE', faculty.event_types.career.StudyLeaveEventHandler), (b'TEACHING', faculty.event_types.awards.TeachingCreditEventHandler), (b'TENUREAPP', faculty.event_types.career.TenureApplicationEventHandler), (b'ACCRED', faculty.event_types.career.AccreditationFlagEventHandler), (b'PROMOTION', faculty.event_types.career.PromotionApplicationEventHandler), (b'SALARYREV', faculty.event_types.career.SalaryReviewEventHandler), (b'CONTRACTRV', faculty.event_types.career.ContractReviewEventHandler), (b'RESUME', faculty.event_types.info.ResumeEventHandler)], max_length=10),
        ),
        migrations.AlterField(
            model_name='eventconfig',
            name='event_type',
            field=models.CharField(choices=[(b'ADMINPOS', faculty.event_types.position.AdminPositionEventHandler), (b'APPOINT', faculty.event_types.career.AppointmentEventHandler), (b'AWARD', faculty.event_types.awards.AwardEventHandler), (b'COMMITTEE', faculty.event_types.info.CommitteeMemberHandler), (b'EXTERN_AFF', faculty.event_types.info.ExternalAffiliationHandler), (b'EXTSERVICE', faculty.event_types.info.ExternalServiceHandler), (b'FELLOW', faculty.event_types.awards.FellowshipEventHandler), (b'GRANTAPP', faculty.event_types.awards.GrantApplicationEventHandler), (b'NORM_TEACH', faculty.event_types.teaching.NormalTeachingLoadHandler), (b'LEAVE', faculty.event_types.career.OnLeaveEventHandler), (b'ONE_NINE', faculty.event_types.teaching.OneInNineHandler), (b'OTHER_NOTE', faculty.event_types.info.OtherEventHandler), (b'LABMEMB', faculty.event_types.info.ResearchMembershipHandler), (b'SALARY', faculty.event_types.career.SalaryBaseEventHandler), (b'STIPEND', faculty.event_types.career.SalaryModificationEventHandler), (b'SPCL_DEAL', faculty.event_types.info.SpecialDealHandler), (b'STUDYLEAVE', faculty.event_types.career.StudyLeaveEventHandler), (b'TEACHING', faculty.event_types.awards.TeachingCreditEventHandler), (b'TENUREAPP', faculty.event_types.career.TenureApplicationEventHandler), (b'ACCRED', faculty.event_types.career.AccreditationFlagEventHandler), (b'PROMOTION', faculty.event_types.career.PromotionApplicationEventHandler), (b'SALARYREV', faculty.event_types.career.SalaryReviewEventHandler), (b'CONTRACTRV', faculty.event_types.career.ContractReviewEventHandler), (b'RESUME', faculty.event_types.info.ResumeEventHandler)], max_length=10),
        ),
        migrations.AlterField(
            model_name='memotemplate',
            name='event_type',
            field=models.CharField(choices=[(b'ADMINPOS', faculty.event_types.position.AdminPositionEventHandler), (b'APPOINT', faculty.event_types.career.AppointmentEventHandler), (b'AWARD', faculty.event_types.awards.AwardEventHandler), (b'COMMITTEE', faculty.event_types.info.CommitteeMemberHandler), (b'EXTERN_AFF', faculty.event_types.info.ExternalAffiliationHandler), (b'EXTSERVICE', faculty.event_types.info.ExternalServiceHandler), (b'FELLOW', faculty.event_types.awards.FellowshipEventHandler), (b'GRANTAPP', faculty.event_types.awards.GrantApplicationEventHandler), (b'NORM_TEACH', faculty.event_types.teaching.NormalTeachingLoadHandler), (b'LEAVE', faculty.event_types.career.OnLeaveEventHandler), (b'ONE_NINE', faculty.event_types.teaching.OneInNineHandler), (b'OTHER_NOTE', faculty.event_types.info.OtherEventHandler), (b'LABMEMB', faculty.event_types.info.ResearchMembershipHandler), (b'SALARY', faculty.event_types.career.SalaryBaseEventHandler), (b'STIPEND', faculty.event_types.career.SalaryModificationEventHandler), (b'SPCL_DEAL', faculty.event_types.info.SpecialDealHandler), (b'STUDYLEAVE', faculty.event_types.career.StudyLeaveEventHandler), (b'TEACHING', faculty.event_types.awards.TeachingCreditEventHandler), (b'TENUREAPP', faculty.event_types.career.TenureApplicationEventHandler), (b'ACCRED', faculty.event_types.career.AccreditationFlagEventHandler), (b'PROMOTION', faculty.event_types.career.PromotionApplicationEventHandler), (b'SALARYREV', faculty.event_types.career.SalaryReviewEventHandler), (b'CONTRACTRV', faculty.event_types.career.ContractReviewEventHandler), (b'RESUME', faculty.event_types.info.ResumeEventHandler)], help_text=b'The type of event that this memo applies to', max_length=10),
        ),
        migrations.AlterField(
            model_name='position',
            name='rank',
            field=models.CharField(blank=True, choices=[(b'LLEC', b'Limited-Term Lecturer'), (b'LABI', b'Laboratory Instructor'), (b'LECT', b'Lecturer'), (b'SLEC', b'Senior Lecturer'), (b'INST', b'Instructor'), (b'ASSI', b'Assistant Professor'), (b'ASSO', b'Associate Professor'), (b'FULL', b'Full Professor'), (b'URAS', b'University Research Associate'), (b'ADJC', b'Adjunct Professor')], max_length=50, null=True),
        ),
    ]
