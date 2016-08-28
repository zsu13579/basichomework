# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_todolist_intime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='intime',
            field=models.DateTimeField(default=b'2016-03-01 0:0:0'),
        ),
    ]
