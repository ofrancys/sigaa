from django.shortcuts import render, redirect, get_object_or_404
from ..models import Aluno
from sigaaa.form import AlunoForm

def alunos(request):
    alunos=Aluno.objects.all()
    context = {
        'alunos' : alunos,
    }
    return render(request, 'aluno/index.html', context)


def add_alunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: message
            return redirect('sigaaa:alunos')
    else:
        form = AlunoForm()
    context = {
        "form": form,
    }
    return render(request, "aluno/add.html", context)


def edit_alunos(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    try:
        if request.method == 'POST':
            form = AlunoForm(request.POST, instance=aluno)
            if form.is_valid():
                form.save()
                alunos = Aluno.objects.all()
                context = {
                    "alunos": alunos
                }
                # TODO: message
                return render(request, "aluno/index.html", context)
        else:
            form = AlunoForm(instance=aluno)
            context = {
                "form": form,
                "aluno_id": aluno_id,
            }
            return render(request, "aluno/edit.html", context)
    except:
        # TODO: message
        return redirect(request, 'sigaaa:alunos')


def delete_alunos(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    aluno.delete()
    return redirect('sigaaa:alunos')