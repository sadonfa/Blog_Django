from blog.models import Category

def get_category(request):
    categories = Category.objects.values_list('id', 'name')

    return {
        'categories': categories
    }