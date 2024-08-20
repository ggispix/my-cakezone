from contacts.models import ContactUs
from subscriptions.forms import SubscriberForm

def contacts(request):
    return{
        'subscribe_users': SubscriberForm(),
        'index_contacts': ContactUs.objects.first()
    }