# Generated by Django 5.0.6 on 2024-06-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
