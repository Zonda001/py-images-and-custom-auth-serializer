# Generated by Django 4.1 on 2024-02-21 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
    ]
