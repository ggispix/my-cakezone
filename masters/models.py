from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='stuff_photos')
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    class Meta:
        verbose_name_plural = 'Staff'
        ordering = ['sort']

    def __str__(self):
        return self.name

