from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('listado_generos', views.lista_generos, name='lista_generos'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
]