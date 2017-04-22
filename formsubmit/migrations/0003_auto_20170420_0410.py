# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsubmit', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default=b'user@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
