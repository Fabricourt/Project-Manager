# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0010_auto_20170728_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-criado_em']},
        ),
    ]
