# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20160601_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='intime',
            field=models.DateTimeField(default=b'2016-06-01 0:0:0'),
        ),
    ]
