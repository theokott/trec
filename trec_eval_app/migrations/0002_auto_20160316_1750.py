# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='dateSubmitted',
            field=models.DateField(default=datetime.date(2016, 3, 16)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dateOfRegistration',
            field=models.DateField(default=datetime.date(2016, 3, 16)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='isFullyAutomated',
            field=models.BooleanField(default=False),
        ),
    ]
