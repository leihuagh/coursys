# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 17:09
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_autoslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='courseoffering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coredata.CourseOffering'),
        ),
        migrations.AlterField(
            model_name='group',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coredata.Member'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(help_text='Group name', max_length=30),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='autoslug', unique_with=('courseoffering',)),
        ),
        migrations.AlterField(
            model_name='group',
            name='svn_slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=17, null=True, populate_from='slug', unique_with=('courseoffering',)),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grades.Activity'),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coredata.Member'),
        ),
    ]
