# Generated by Django 5.0 on 2024-10-31 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigaaa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='valor1',
            new_name='nota1',
        ),
        migrations.RenameField(
            model_name='nota',
            old_name='valor2',
            new_name='nota2',
        ),
    ]