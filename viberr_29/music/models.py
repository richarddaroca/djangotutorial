from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

#each class will make its own table

# note https://docs.djangoproject.com/en/1.11/topics/db/queries/
# note every time we add a new table we need to do the migrations

class Album(models.Model):                          # every model you create it has to inherit from models.Model
    artist = models.CharField(max_length=250)       # artist will be the colomn name in our table in DB
    album_title = models.CharField(max_length=500)  # <name of colomn> = models.<datatype>
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()                 # this will as for a file

    def get_absolute_url(self):                             # this tells us that after we submit a new album it will send it to the return value
        return reverse('music:detail', kwargs={'pk':self.pk})  # since we need to pass the pk we use kwargs={'pk':self.pk} since this field is hidden in line 11-15
                                                            # we pass the pk since when we view details we want it to show us the one we selected
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # foreignkey is = to the primary key of the album since
    file_type = models.CharField(max_length=10)                 # each song will belong to 1 album
    song_title = models.CharField(max_length=250)               # on_delete=models.CASCADE - will delete all the songs
    is_favorite = models.BooleanField(default=False)            # when the album it belongs to is deleted

    def __str__(self):
        return self.song_title