from .models import Staff

def staff(request):
    return{
        'index_masters': Staff.objects.filter(is_visible=True),
    }