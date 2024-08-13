from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        return iter(self.dishes.filter(is_visible=True))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('sort',)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='dish/')
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    sort = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ['sort']