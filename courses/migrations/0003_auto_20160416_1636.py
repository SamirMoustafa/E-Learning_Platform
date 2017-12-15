from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160415_2108'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeleteChapter',
        ),
        migrations.DeleteModel(
            name='DeleteCourse',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='textblock',
            name='text_block_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Chapter'),
        ),
        migrations.AlterField(
            model_name='ytlink',
            name='yt_link_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Chapter'),
        ),
    ]
