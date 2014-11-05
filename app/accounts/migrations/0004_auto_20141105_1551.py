# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_uploadedfile_upload_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='description',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='upload',
            field=models.FileField(upload_to=accounts.models.upload_path),
        ),
    ]
