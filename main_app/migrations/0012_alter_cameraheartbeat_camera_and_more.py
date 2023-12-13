# Generated by Django 4.2.7 on 2023-12-11 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_cameraheartbeat_report_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameraheartbeat',
            name='camera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heartbeats', to='main_app.camera'),
        ),
        migrations.AlterField(
            model_name='counterhistory',
            name='camera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counter_histories', to='main_app.camera'),
        ),
    ]