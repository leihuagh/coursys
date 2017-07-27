# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 14:54
from __future__ import unicode_literals

import courselib.json_fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coredata', '0018_add_course_descriptions'),
        ('tacontracts', '0006_auto_20151216_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text=b"Description of the work for a course, as it will appear on the contract. (e.g. 'Office/marking')", max_length=60)),
                ('hidden', models.BooleanField(default=False)),
                ('config', courselib.json_fields.JSONField(default={})),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description_unit', to='coredata.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='tacourse',
            name='description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tacontracts.CourseDescription'),
        ),
    ]