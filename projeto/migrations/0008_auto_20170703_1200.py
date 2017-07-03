# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0007_auto_20170703_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participacao',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='projeto.Equipe'),
        ),
        migrations.AlterField(
            model_name='participacao',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacoes', to='projeto.Funcionario'),
        ),
    ]
