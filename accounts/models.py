from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models
from location_field.models.spatial import LocationField

class CustomUser(AbstractUser):

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to='static/images', blank=True, null=True)
    city = models.CharField(max_length=255)
    location = LocationField(
        based_fields=['city'], zoom=7, default=Point(1.0, 1.0))

    def __str__(self):
        return self.user.username

    @property
    def get_picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return "/static/images/user.jpg"
