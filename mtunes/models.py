from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 2000)
    singer = models.CharField(max_length= 2000)
    tags = models.CharField(max_length= 100)
    image = models.ImageField(upload_to = 'docs')
    song = models.FileField(upload_to= 'docs')
    movie = models.CharField(max_length = 150, default = "None")


    def __str__(self):
        return self.name
class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")
