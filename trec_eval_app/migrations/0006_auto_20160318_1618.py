# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trec_eval_app', '0005_auto_20160317_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='feedbackType',
            field=models.CharField(default=b'n', max_length=9, choices=[(b'n', b'None'), (b'p', b'Pseudo'), (b'r', b'Relevance'), (b'o', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='queryType',
            field=models.CharField(default=b't', max_length=1, choices=[(b't', b'Title'), (b'td', b'Title and Description'), (b'd', b'Description'), (b'a', b'All'), (b'o', b'Other')]),
        ),
    ]
