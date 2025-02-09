from django.contrib import admin

# Primeiro vamos importar o modelo Contact
from contact import models

# Register your models here.

# Agora vamos registrar o modelo Contact no admin e isso aparecerá no painel de administração
# vamos colocar um decorador para registrar o modelo Contact
@admin.register( models.Contact)
class ContactAdmin( admin.ModelAdmin ):
    # No painel adm, essa função que mostra uma lista mas pode ser uma tupla, mostra em ordem e com o nomes passados
    list_display = ['id','first_name', 'last_name', 'email', 'phone']
    # O "-" é um sinal de ordenação
    ordering = ['-id']
    # Aqui mostra um campo de pesquisa e por quais itens podemos pesquisar.
    search_fields = ['id','first_name', 'last_name', 'email']
    #list_filter = ['created_date']