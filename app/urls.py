from django.contrib import admin
from django.urls import path
from contatos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('salvar/', views.salvar, name='salvar'),
    path('excluir/<int:id>/', views.excluir, name='excluir'), # Nova rota com parâmetro
]