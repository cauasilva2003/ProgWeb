"""
URL configuration for distribuicao_grupos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('admin/', admin.site.urls),
    path('tema/cadastrar/', views.cadastrar_tema, name='cadastrar_tema'),
    path('tema/<int:tema_id>/distribuir/', views.distribuir_grupos, name='distribuir_grupos'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/<int:aluno_id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:aluno_id>/deletar/', views.deletar_aluno, name='deletar_aluno'),
    path('temas/', views.listar_temas, name='listar_temas'),
    path('temas/<int:tema_id>/deletar/', views.deletar_tema, name='deletar_tema'),
    path('tema/<int:tema_id>/grupos/', views.listar_grupos, name='listar_grupos'),
]
