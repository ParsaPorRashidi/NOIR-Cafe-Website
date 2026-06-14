from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MusicTrack


class PlaylistListView(APIView):
    def get(self, request, format=None):
        tracks = MusicTrack.objects.all()

        playlist = []
        for track in tracks:
            playlist.append({
                'name': track.name,
                'artist': track.artist,
                'src': track.audio_file.url if track.audio_file else None,
                'cover_image': track.cover_image.url if track.cover_image else None
            })

        return Response({'playlist': playlist})