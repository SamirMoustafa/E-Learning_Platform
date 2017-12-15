from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20160420_1812'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddStudents',
        ),
    ]
