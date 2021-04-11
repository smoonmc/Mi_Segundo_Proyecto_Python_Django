from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User #Este impor sirve para utilizar la autntificación de usuario que trae por defecto el admin de Django

# Create your models here.
#Tabla de la BD
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)   
    catgories = models.ManyToManyField(Category, verbose_name='Categorias', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')


    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at'] #ordena en forma descendente, del mas nuevo al mas viejo

    def __str__(self):
        return self.title