# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0002_auto_20160316_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='dateSubmitted',
            field=models.DateField(null=True),
        ),
    ]
