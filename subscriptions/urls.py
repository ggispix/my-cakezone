from django.urls import path
from .views import subscribe
app_name = 'subscriptions'
urlpatterns = [
    path('subscriptions/', subscribe, name='subscribe'),
]
