from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_delete_addstudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='textblock',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 24, 17, 40, 54, 345815, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ytlink',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 24, 17, 41, 11, 187939, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
