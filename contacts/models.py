from django.db import models

# Create your models here.
class ContactUs(models.Model):
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)
    phone_numbers = models.CharField(max_length=50)

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return f'{self.city}, {self.street_address}'
