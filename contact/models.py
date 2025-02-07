from django.db import models
from django.utils import timezone
# Create your models here.
# Criando as minha primeira tabela
# primeiro nome (string de  50 caracteres)
# sobrenome (string de 50 caracteres)
# telefone (string de 50 caracteres)
# email (string de 100 caracteres)
# data de criação (data e hora)
# descrição (texto)

class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50, blank = True)
    phone = models.CharField( max_length = 50)
    email = models.CharField( max_length = 254, blank = True)
    created_date = models.DateTimeField( timezone.now )
    description = models.TextField()