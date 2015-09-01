# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150125_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('duration', models.PositiveIntegerField(default=300, help_text=b'Enter the task duration in seconds')),
                ('progress', models.PositiveIntegerField(default=0)),
                ('job_id', models.CharField(max_length=128)),
                ('result', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
