from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactUs
from .forms import MessageFromCustomerForm
# from .forms import SubscribeUserForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    contacts = ContactUs.objects.filter(is_visible=True)
    context = {
        # 'subscribe_users': SubscribeUserForm.objects.all(),
        'message_form': MessageFromCustomerForm(),
        'contacts': contacts
    }
    return render(request, 'contacts.html', context=context)
