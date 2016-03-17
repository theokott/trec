# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0003_auto_20160317_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dateOfRegistration',
            field=models.DateField(null=True),
        ),
    ]
