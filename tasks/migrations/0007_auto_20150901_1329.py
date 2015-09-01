# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_longtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longtask',
            name='name',
            field=models.CharField(help_text=b'Enter a unique name for the task', max_length=128),
            preserve_default=True,
        ),
    ]
