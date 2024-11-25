# Generated by Django 5.0 on 2024-10-31 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('matricula', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_professor', models.CharField(max_length=100)),
                ('carga_horaria', models.IntegerField()),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('valor2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigaaa.aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigaaa.disciplina')),
            ],
        ),
    ]