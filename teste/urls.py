"""
URL configuration for teste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from aplicativo import views


urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/atualizar/<int:usuario_id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/deletar/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/cadastrar/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
]
