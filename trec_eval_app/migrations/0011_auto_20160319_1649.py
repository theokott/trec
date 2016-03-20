# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0010_runscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runscore',
            name='run',
        ),
        migrations.DeleteModel(
            name='RunScore',
        ),
        migrations.RemoveField(
            model_name='run',
            name='track',
        ),
        migrations.RemoveField(
            model_name='track',
            name='slug',
        ),
    ]
