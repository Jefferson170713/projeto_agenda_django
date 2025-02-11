from django.contrib import admin # type: ignore

# Primeiro vamos importar o modelo Contact
from contact import models


# Agora vamos registrar o modelo Contact no admin e isso aparecerá no painel de administração
# vamos colocar um decorador para registrar o modelo Contact
@admin.register( models.Contact)
class ContactAdmin( admin.ModelAdmin ):
    # No painel adm, essa função que mostra uma lista mas pode ser uma tupla, mostra em ordem e com o nomes passados
    list_display = ['id','first_name', 'last_name', 'phone', 'show']
    # O "-" é um sinal de ordenação do último adicionado para o primeiro adicionado
    ordering = ['-id']
    # Aqui mostra um campo de pesquisa e por quais itens podemos pesquisar.
    search_fields = ['id','first_name', 'last_name']
    # paginação dos das tabelas na página de administração
    list_per_page = 10
    list_max_show_all = 200
    # filtro de data, mas não vou colocar porque ocupa espaço.
    #list_filter = ['created_date']
    # liks para editar o contato
    list_editable = ['first_name', 'last_name', 'show']
    list_display_links = ['id','phone']
    

@admin.register( models.Category )
class CategoryAdmin( admin.ModelAdmin ):
    list_display = 'id', 'name',
    list_display_links = 'id', 'name',