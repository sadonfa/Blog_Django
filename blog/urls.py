from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.list, name="list-article"),
    path('categoria/<int:id>', views.category, name="category"),
    path('articulo/<int:article_id>', views.article, name="article" )  
]
