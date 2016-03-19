# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0008_auto_20160319_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='track',
            field=models.ForeignKey(default=0, to='trec_eval_app.Track'),
            preserve_default=False,
        ),
    ]
