from .models import Category, Dish

def category(request):
    return{
        'index_menu': Category.objects.filter(is_visible=True),
    }