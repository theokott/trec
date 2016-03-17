# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0004_auto_20160317_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='dateSubmitted',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dateOfRegistration',
        ),
    ]
