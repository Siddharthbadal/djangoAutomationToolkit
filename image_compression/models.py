from django.db import models
from django.contrib.auth.models import User 

class CompressImage(models.Model):
    CHOICES = [(i,i) for i in range(10,101, 10)]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to='original_images/')
    quality = models.IntegerField(choices=CHOICES)
    compressed_image = models.ImageField(upload_to='compressed_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username