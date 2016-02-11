# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Render',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(blank=True, default='')),
                ('file_type', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_tablespace': 'ut_space',
                'db_table': 'ut_render',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_tablespace': 'ut_space',
                'db_table': 'ut_templates',
            },
        ),
        migrations.AddField(
            model_name='render',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usertemplates.Template'),
        ),
    ]
