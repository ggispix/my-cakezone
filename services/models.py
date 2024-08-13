from django.db import models

# Create your models here.
class OurService(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Our Services'
        ordering = ('sort',)