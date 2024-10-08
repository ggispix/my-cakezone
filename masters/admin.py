from django.contrib import admin
from .models import Staff
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'position', 'is_visible')
    search_fields = ('name', 'position')
    list_filter = ('is_visible',)
    list_editable = ('name', 'position', 'is_visible')

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width= "50" height="50"/>')

    photo_tag.short_description = 'Photo'
