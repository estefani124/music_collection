from django.urls import include, path
from rest_framework import routers
from .views import GenreViewSet, ArtistViewSet, AlbumViewSet, AlbumArtistViewSet

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'album-artists', AlbumArtistViewSet)

urlpatterns = [
    path("api/v1/",include(router.urls))
]