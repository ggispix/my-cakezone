
from django.shortcuts import render, redirect
from .forms import SubscriberForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})

# Create your views here.
