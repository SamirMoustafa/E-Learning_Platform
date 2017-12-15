from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160416_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytlink',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
