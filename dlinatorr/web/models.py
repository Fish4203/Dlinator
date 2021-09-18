from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Torrent(models.Model):
    title = models.CharField(max_length=200)
    magnet = models.CharField(max_length=500)
    cat = models.CharField(max_length=200)
    dateAdd = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
