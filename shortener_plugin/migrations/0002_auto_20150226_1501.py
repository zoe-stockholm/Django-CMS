# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('shortener_plugin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortenerplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='shortenerplugin',
            name='url_pair',
        ),
        migrations.DeleteModel(
            name='ShortenerPlugin',
        ),
    ]
