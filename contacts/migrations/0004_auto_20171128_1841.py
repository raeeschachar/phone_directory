# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20171128_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip',
        ),
        migrations.AddField(
            model_name='address',
            name='address_selection',
            field=models.CharField(choices=[(b'HOME', b'Home Address'), (b'OFFICE', b'Office Address')], default=b'HOME', max_length=2),
        ),
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default=12345, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=15),
        ),
    ]
