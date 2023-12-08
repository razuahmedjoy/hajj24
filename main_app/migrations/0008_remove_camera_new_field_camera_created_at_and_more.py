# Generated by Django 4.2.7 on 2023-12-08 16:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_camera_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='new_field',
        ),
        migrations.AddField(
            model_name='camera',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='camera',
            name='heart_beat_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='camera',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='sn',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='camera',
            name='tent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.tent'),
        ),
    ]
