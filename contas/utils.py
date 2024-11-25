from django.contrib.messages import constants
from django.contrib import messages


def password_is_valid(request, password, confirm_password):
    if len(password) < 3:
        messages.add_message(request, constants.ERROR, 'A senha deve ter no mínimo 3 caracteres')
        return False
    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
        return False
    return True