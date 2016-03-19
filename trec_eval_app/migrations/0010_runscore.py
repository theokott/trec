# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0009_run_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('run', models.OneToOneField(to='trec_eval_app.Run')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
