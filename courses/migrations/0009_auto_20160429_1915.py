from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20160424_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textblock',
            old_name='chapter_description',
            new_name='lesson',
        ),
    ]
