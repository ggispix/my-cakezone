from django import forms
from .models import MessagesFromCustomers
#from .models import SubscribeUser

class MessageFromCustomerForm(forms.ModelForm):
    class Meta:
        model = MessagesFromCustomers
        fields = ('name', 'email','subject','message')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4',
                                           'placeholder':'Name',
                                           'style':'height: 55px;',}),
            'email': forms.EmailInput(attrs={'class':'form-control bg-light border-0 px-4',
                                           'placeholder':'Email',
                                           'style':'height: 55px;',}),
            'subject': forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4',
                                              'placeholder':'Subject',
                                              'style':'height: 55px;',}),
            'message': forms.Textarea(attrs={'class':'form-control bg-light border-0 px-4 py-3',
                                             'rows': 4,
                                             'placeholder':'Message'}),
        }

# class SubscribeUserForm(forms.ModelForm):
#     class Meta:
#         model = SubscribeUser
#         fields = ('email',)
#
#         widgets = {
#             'email' : forms.EmailInput(attrs={'class':'form-control border-white p-3',
#                                               'placeholder':"Your Email",})
#         }