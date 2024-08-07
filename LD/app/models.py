from django.db import models

# Create your models here.
class YT_Converter(models.Model):
    # id = models.AutoField()
    link = models.TextField()
    mp3 = models.FileField( upload_to='MP3', max_length=100)
    mp4 = models.FileField( upload_to='MP4', max_length=100)