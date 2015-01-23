# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='job_id',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
