# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0006_auto_20160318_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='feedbackType',
            field=models.CharField(default=b'n', max_length=1, choices=[(b'n', b'None'), (b'p', b'Pseudo'), (b'r', b'Relevance'), (b'o', b'Other')]),
        ),
        migrations.AlterField(
            model_name='run',
            name='queryType',
            field=models.CharField(default=b't', max_length=2, choices=[(b't', b'Title'), (b'td', b'Title and Description'), (b'd', b'Description'), (b'a', b'All'), (b'o', b'Other')]),
        ),
    ]
