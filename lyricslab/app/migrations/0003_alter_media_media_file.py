# Generated by Django 5.0.1 on 2024-01-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_media_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media_file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
