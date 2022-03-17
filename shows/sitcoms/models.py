from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Show(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.title