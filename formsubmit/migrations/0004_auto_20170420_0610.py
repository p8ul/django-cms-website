# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsubmit', '0003_auto_20170420_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(max_length=120, choices=[(b'Single', b'Single Room'), (b'Double', b'Double Rooms'), (b'Triple', b'Triple Rooms'), (b'Ensuite', b'Ensuite')]),
        ),
    ]
