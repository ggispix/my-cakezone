from .models import OurService

def service(request):
    return{
        'index_service': OurService.objects.filter(is_visible=True),
    }