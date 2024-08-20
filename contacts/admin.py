from django.contrib import admin
from .models import ContactUs, MessagesFromCustomers
# from subscriptions.models import  Subscriber
# Register your models here.
from django.utils.safestring import mark_safe
@admin.register(ContactUs)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id','city', 'street_address','email', 'is_visible')
    search_fields = ('city', 'phone_number', 'email')
    list_filter = ('is_visible',)
    list_editable = ('city', 'street_address','email', 'is_visible')

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width= "50" height="50"/>')

    photo_tag.short_description = 'Photo'

admin.site.register(MessagesFromCustomers)
# admin.site.register(Subscriber)