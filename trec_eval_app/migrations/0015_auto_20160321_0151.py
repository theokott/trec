# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0014_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='MAPScore',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='run',
            name='P10Score',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='run',
            name='P20Score',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
        ),
    ]
