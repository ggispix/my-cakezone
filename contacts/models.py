from django.db import models

# class SubscribeUser(models.Model):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         verbose_name = 'Email for subscribe'
#         verbose_name_plural = 'Emails for subscribes'




class MessagesFromCustomers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()


    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = 'Message from Customer'
        verbose_name_plural = 'Messages from Customers'

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
        return self.street_address

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contacts'
