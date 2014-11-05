# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='upload_dt',
            field=models.DateTimeField(default=datetime.date(2014, 11, 5), auto_now_add=True),
            preserve_default=False,
        ),
    ]
