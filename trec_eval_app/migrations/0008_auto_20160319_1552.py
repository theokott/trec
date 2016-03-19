# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0007_auto_20160318_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='adminPermission',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
