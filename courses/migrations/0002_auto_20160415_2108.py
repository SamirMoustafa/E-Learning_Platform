from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DeleteCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='created_date',
            new_name='chapter_created_date',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='course_fk',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='created_date',
            new_name='course_created_date',
        ),
        migrations.RenameField(
            model_name='textblock',
            old_name='text_area_fk',
            new_name='text_block_fk',
        ),
        migrations.RenameField(
            model_name='ytlink',
            old_name='youtube_fk',
            new_name='yt_link_fk',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_link',
        ),
        migrations.RemoveField(
            model_name='course',
            name='user_fk',
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='textblock',
            name='chapter_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ytlink',
            name='link',
            field=models.URLField(default='', unique=True),
        ),
    ]
