# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0015_auto_20160321_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='MAPScore',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='P10Score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='P20Score',
            field=models.FloatField(null=True),
        ),
    ]
