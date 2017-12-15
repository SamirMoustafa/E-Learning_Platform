from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_for_everybody'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
