from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20160429_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='for_everybody',
            field=models.BooleanField(default=True),
        ),
    ]
