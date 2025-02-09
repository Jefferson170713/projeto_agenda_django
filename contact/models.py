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
    email = models.EmailField( max_length = 254, blank = True)
    created_date = models.DateTimeField( default = timezone.now )
    description = models.TextField( blank = True)

    # Aqui vamos definir os campos que queremos que apareçam no painel de administração
    # Este é o campo que será exibido na lista de contatos, mas podemos mudar o que aparece no painel de administração
    def __str__( self ) -> str:
        #return super().__str__( f'{self.first_name} {self.last_name}' )
        return f'{self.first_name} {self.last_name} - {self.email}'