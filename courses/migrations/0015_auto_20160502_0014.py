from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20160501_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
