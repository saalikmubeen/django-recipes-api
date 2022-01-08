# Generated by Django 3.2.4 on 2022-01-08 23:31

from django.db import migrations, models
import shared.models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=shared.models.recipe_image_file_path),
        ),
    ]
