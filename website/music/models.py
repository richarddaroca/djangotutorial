from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 50)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.album_title + " - " + self.artist

#pk - primary key is added by dango automatically for each set of albums (id number)
#example. the album Red has a pk = 1

#fk - foreign key is used in Song so that wathever the songe that has the fk of 1 would be assinged to the album Red
# the songs that belong to the album red should also have a foreign key of 1
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # on_delete - if ever we delete an album all the songs that belongs to it would also be deleted.
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)
