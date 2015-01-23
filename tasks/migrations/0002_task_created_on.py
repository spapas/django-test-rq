# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 23, 18, 30, 42, 283935, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
