# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runID', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('isFullyAutomated', models.BooleanField()),
                ('queryType', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'example 1'), (b'b', b'example 2')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskID', models.CharField(unique=True, max_length=128)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trackID', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='track',
            field=models.ForeignKey(to='trec_eval_app.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='run',
            name='task',
            field=models.ForeignKey(to='trec_eval_app.Task'),
            preserve_default=True,
        ),
    ]
