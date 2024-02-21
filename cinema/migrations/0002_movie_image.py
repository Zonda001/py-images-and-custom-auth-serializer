# Generated by Django 4.1 on 2024-02-20 17:57
import os
from uuid import uuid4
from django.utils.text import slugify
import cinema.models
from django.db import migrations, models


def generate_image_filename(instance, filename):
    """
    Generate a unique filename for the Movie model's image field.
    Format: "{slugified_movie_title}-{uuid}{file_extension}"
    """
    # Get the file extension from the original filename
    _, file_extension = os.path.splitext(filename)

    # Generate a unique identifier using uuid4
    unique_identifier = str(uuid4())

    # Get the slugified version of the movie title
    movie_title_slugified = slugify(instance.title)

    # Construct the final filename
    final_filename = f"{movie_title_slugified}-{unique_identifier}{file_extension}"

    return final_filename


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cinema.models.Movie.generate_image_filename),
        ),
    ]