import io
from django.db import models
from django.core.files import File
from mutagen.id3 import ID3, TIT2, TPE1, APIC
from mutagen.mp3 import MP3


class MusicTrack(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام آهنگ", blank=True)
    artist = models.CharField(max_length=200, verbose_name="هنرمند", blank=True)
    audio_file = models.FileField(upload_to='music/', verbose_name="فایل صوتی")
    cover_image = models.ImageField(upload_to='music/covers/', blank=True, null=True, verbose_name="تصویر کاور")

    class Meta:
        verbose_name = 'موزیک'
        verbose_name_plural = 'موزیک ها'

    def __str__(self):
        return f"{self.name or 'نامشخص'} - {self.artist or 'نامشخص'}"

    def save(self, *user_args, **user_kwargs):
        if self.audio_file and not self.name:
            try:
                audio = ID3(self.audio_file.file)

                if 'TIT2' in audio:
                    self.name = str(audio['TIT2'].text[0])

                if 'TPE1' in audio:
                    self.artist = str(audio['TPE1'].text[0])

                for tag in audio.values():
                    if isinstance(tag, APIC):
                        image_data = tag.data
                        image_file = io.BytesIO(image_data)

                        filename = f"{self.name or 'cover'}.jpg"
                        self.cover_image.save(filename, File(image_file), save=False)
                        break
            except Exception as e:
                print(f"خطا در استخراج متادیتا: {e}")

            if not self.name:
                self.name = self.audio_file.name.split('/')[-1]

        super().save(*user_args, **user_kwargs)