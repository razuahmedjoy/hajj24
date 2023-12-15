# Generated by Django 4.2.7 on 2023-11-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_tent_air_condition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=255)),
                ('tent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cameras', to='main_app.tent')),
            ],
        ),
    ]
