from django.contrib import admin
from .models import MusicTrack


@admin.register(MusicTrack)
class MusicTrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'audio_file_preview')

    search_fields = ('name', 'artist')

    def audio_file_preview(self, obj):
        return obj.audio_file.name if obj.audio_file else "بدون فایل"

    audio_file_preview.short_description = "نام فایل"

    fields = ('name', 'artist', 'audio_file', 'cover_image')