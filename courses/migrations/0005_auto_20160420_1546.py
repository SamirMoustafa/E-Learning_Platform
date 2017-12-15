from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20160416_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytlink',
            name='link',
            field=models.URLField(),
        ),
    ]
