from django.db import models

class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        default='M'
    )
    
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    ano = models.DateField()

    def __str__(self):
        return self.nome


class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina.nome}"
