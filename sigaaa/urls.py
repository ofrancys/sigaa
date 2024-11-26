from django.urls import path
from .views import view, view_alunos, view_disciplinas, view_notas 

app_name="sigaaa"

urlpatterns = [
    path('', view.base_view, name='base_view'),

    path('alunos/', view_alunos.alunos, name='alunos'),
    path('add_alunos', view_alunos.add_alunos, name='add_alunos'),
    path('edit_alunos/<int:aluno_id>', view_alunos.edit_alunos, name='edit_alunos'),
    path('delete_alunos/<int:aluno_id>', view_alunos.delete_alunos, name='delete_alunos'),

    path('disciplinas/', view_disciplinas.disciplinas, name='disciplinas'),
    path('add_disciplinas', view_disciplinas.add_disciplinas, name='add_disciplinas'),
    path('edit_disciplinas/<int:disciplina_id>', view_disciplinas.edit_disciplinas, name='edit_disciplinas'),
    path('delete_disciplinas/<int:disciplina_id>', view_disciplinas.delete_disciplinas, name='delete_disciplinas'),

    path('notas/', view_notas.notas, name='notas'),
    path('add_notas', view_notas.add_notas, name='add_notas'),
    path('edit_notas/<int:nota_id>', view_notas.edit_notas, name='edit_notas'),
    path('delete_notas/<int:nota_id>', view_notas.delete_notas, name='delete_notas'),

    #path('notas/', notas.index, name='nota_lista'),
]