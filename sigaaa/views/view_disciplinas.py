from django.shortcuts import render, redirect, get_object_or_404
from ..models import Disciplina
from sigaaa.form import DisciplinaForm

def disciplinas(request):
    disciplinas=Disciplina.objects.all()
    context = {
        'disciplinas' : disciplinas,
    }
    return render(request, 'disciplina/index.html', context)


def add_disciplinas(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: message
            return redirect('sigaaa:disciplinas')
    else:
        form = DisciplinaForm()
    context = {
        "form": form,
    }
    return render(request, "disciplina/add.html", context)


def edit_disciplinas(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    try:
        if request.method == 'POST':
            form = DisciplinaForm(request.POST, instance=disciplina)
            if form.is_valid():
                form.save()
                disciplinas = Disciplina.objects.all()
                context = {
                    "disciplinas": disciplinas
                }
                # TODO: message
                return render(request, "disciplina/index.html", context)
        else:
            form = DisciplinaForm(instance=disciplina)
            context = {
                "form": form,
                "disciplina_id": disciplina_id,
            }
            return render(request, "disciplina/edit.html", context)
    except:
        # TODO: message
        return redirect(request, 'sigaaa:disiciplnas')
 
    
def delete_disciplinas(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    disciplina.delete()
    return redirect('sigaaa:disciplinas')