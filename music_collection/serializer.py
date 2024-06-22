from rest_framework import serializers
from .models import Genre, Album, Artist, AlbumArtist
from django.conf import settings

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Album
        fields = '__all__'
    
    def create(self, validated_data):
        image = validated_data.pop('image', None)
        album = super().create(validated_data)       
        if image:
            album.image_url = self.save_image(album,image)
            album.save()
            return album
        
        
    def save_image(self, album, image):
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        import os
    
        path = default_storage.save(os.path.join('images', str(album.id) + '_' + image.
        name), ContentFile(image.read()))
        return settings.MEDIA_URL + path
    
        
class AlbumArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumArtist
        fields = '__all__'