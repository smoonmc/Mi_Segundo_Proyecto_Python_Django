from django.shortcuts import render, get_object_or_404 # el 404 es para desplegaruna pagina de error con este número.
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def list(request):

    #sacar articulos
    article = Article.objects.all()

    #Paginar los articulos
    paginator = Paginator(article, 2) 

    #Recoger numero página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })

@login_required(login_url="login")
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
   #articles = Article.objects.filter(catgories=category)

    return render(request, 'categories/category.html',{
        'category': category
     #   'articles': articles
    })

@login_required(login_url="login")
def article(request, article_id):

    articulo = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
        'article':articulo
    })