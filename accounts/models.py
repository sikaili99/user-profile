from django.contrib.auth.models import User
from django.contrib.gis.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.user.username
