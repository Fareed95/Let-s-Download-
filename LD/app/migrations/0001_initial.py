# Generated by Django 5.0.6 on 2024-08-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YT_Converter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('mp3', models.FileField(upload_to='MP3')),
                ('mp4', models.FileField(upload_to='MP4')),
            ],
        ),
    ]
