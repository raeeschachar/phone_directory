# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-09 09:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_selection', models.CharField(choices=[(b'home', b'Home Address'), (b'office', b'Office Address')], default=b'home', max_length=6)),
                ('address_line', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 20 digits allowed.", regex=b'^\\+?1?\\d{9,20}$')])),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact'),
        ),
    ]
