from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

class Album(models.Model):
    title = models.CharField(max_length=255)
    songs = models.TextField(blank=True)
    publication_date = models.DateField()
    image_url = models.URLField(max_length=255, blank=True, null=True)
    genre = models.ForeignKey (Genre, on_delete=models.CASCADE)
    
class AlbumArtist(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)