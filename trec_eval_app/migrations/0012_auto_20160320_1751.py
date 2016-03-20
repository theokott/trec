# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0011_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='MAPScore',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='run',
            name='P10Score',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='run',
            name='P20Score',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=b'profile_images/default.png', upload_to=b'profile_images', blank=True),
        ),
    ]
