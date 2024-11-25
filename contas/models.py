from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True)

    def __str__(self):
     return self.user.username


