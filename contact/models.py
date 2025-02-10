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
# Isso será feito depois, que é a criação da coluna show
# vamos criar uma nova classe que será usado como chave estrangeira
# para criar um owner para cada contato que for criado
from django.contrib.auth.models import User

class Category(models.Model):
    # Aqui para mostrar o nome no painel de administração
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField( max_length = 50)
    # somente para retornar o nome da categoria
    def __str__( self ) -> str:
        return self.name
class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50, blank = True)
    phone = models.CharField( max_length = 50)
    email = models.EmailField( max_length = 254, blank = True)
    created_date = models.DateTimeField( default = timezone.now )
    description = models.TextField( blank = True)

    show = models.BooleanField( default =  True )
    picture = models.ImageField( upload_to = 'pictures/%Y/%m/%d/', blank = True) # instalar o pillow
    # vamos criar a parte de conexão com a chave estrangeira
    # on_delete = models.DO_NOTHING, significa que se a categoria for deletada, os contatos não serão deletados
    category = models.ForeignKey( Category, on_delete = models.SET_NULL, blank = True, null = True) 
    owner = models.ForeignKey( User, on_delete = models.SET_NULL, blank = True, null = True)
    # Aqui vamos definir os campos que queremos que apareçam no painel de administração
    # Este é o campo que será exibido na lista de contatos, mas podemos mudar o que aparece no painel de administração
    def __str__( self ) -> str:
        #return super().__str__()
        return f'{self.first_name} {self.last_name} - {self.email}'

