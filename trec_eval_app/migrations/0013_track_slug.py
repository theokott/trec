# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0012_auto_20160319_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
