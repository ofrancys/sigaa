from django.shortcuts import render, redirect, get_object_or_404
from ..models import Nota
from sigaaa.form import NotaForm

def notas(request):
    notas = Nota.objects.all()
    context = {
        'notas': notas,
    }
    return render(request, 'nota/index.html', context)

def add_notas(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sigaaa:notas')
    else:
        form = NotaForm()
    context = {
        "form": form,
    }
    return render(request, "nota/add.html", context)

def edit_notas(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    try:
        if request.method == 'POST':
            form = NotaForm(request.POST, instance=nota)
            if form.is_valid():
                form.save()
                notas = Nota.objects.all()
                context = {
                    "notas": notas
                }
                return render(request, "nota/index.html", context)
        else:
            form = NotaForm(instance=nota)
            context = {
                "form": form,
                "nota_id": nota_id,
            }
            return render(request, "nota/edit.html", context)
    except:
        return redirect('sigaaa:notas')

def delete_notas(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    nota.delete()
    return redirect('sigaaa:notas')