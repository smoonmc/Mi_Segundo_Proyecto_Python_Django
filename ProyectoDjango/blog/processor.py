from blog.models import Category,Article

def get_categories(request):

    ids_in_use = Article.objects.filter(public=True).values_list('catgories',flat=True)

    categorias = Category.objects.filter(id__in=ids_in_use).values_list('id', 'name')

    return {
        'categories':categorias,
        'ids':ids_in_use
    }