from django.urls import path
from .views import PlaylistListView

urlpatterns = [
    path('api/playlist/', PlaylistListView.as_view(), name='playlist_api'),
]