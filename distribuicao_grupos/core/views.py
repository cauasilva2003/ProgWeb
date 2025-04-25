from django.shortcuts import render, redirect, get_object_or_404
from .forms import TemaForm, AlunoForm
from .models import Tema, Aluno, Grupo
from .utils import alocar_alunos_e_sortear_grupos

def home(request):
    return render(request, 'core/home.html')

def cadastrar_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save()
            return redirect('distribuir_grupos', tema_id=tema.id)
    else:
        form = TemaForm()
    return render(request, 'core/cadastrar_tema.html', {'form': form})

def distribuir_grupos(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)

    # Apaga os grupos anteriores
    Grupo.objects.filter(tema=tema).delete()

    # Pega todos os alunos atuais
    alunos = list(Aluno.objects.all())
    distribuicoes = alocar_alunos_e_sortear_grupos(tema, alunos)

    # Cria novos grupos
    for dist in distribuicoes:
        grupo = Grupo.objects.create(
            tema=tema,
            nome=dist['nome'],
            horario_apresentacao=dist['horario'],
            ordem_apresentacao=dist['ordem']
        )
        grupo.alunos.set(dist['alunos'])

    return redirect('listar_grupos', tema_id=tema.id)

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'core/cadastrar_aluno.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'core/listar_alunos.html', {'alunos': alunos})

def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'core/cadastrar_aluno.html', {'form': form})

def deletar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.delete()
    return redirect('listar_alunos')

def listar_temas(request):
    temas = Tema.objects.all()
    return render(request, 'core/listar_temas.html', {'temas': temas})

from django.shortcuts import get_object_or_404

def deletar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    tema.delete()
    return redirect('listar_temas')

def listar_grupos(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    grupos = Grupo.objects.filter(tema=tema).order_by('ordem_apresentacao')
    return render(request, 'core/listar_grupos.html', {'tema': tema, 'grupos': grupos})




