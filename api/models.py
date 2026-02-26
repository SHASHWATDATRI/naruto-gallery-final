from django.db import models

# Create your models here.
from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField() # Placeholder ya Cloudinary link ke liye

    def __str__(self):
        return self.title