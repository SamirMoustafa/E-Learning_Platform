from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20160430_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=b'')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('file_fk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Chapter')),
            ],
        ),
    ]
