from django.shortcuts import render, get_object_or_404 # type: ignore
from django.http import Http404 # type: ignore
# agora vamos importar o modelo Contact para que possamos exibir os dados na página
from contact.models import Contact
# Create your views here.
def index(request):
    # Recebendo todos os contatos que temos no banco de dados e ordenando pelo id de forma decrescente
    #contacts = Contact.objects.all().order_by('-id')
    # filtrando os contatos que estão marcados como show=True, e pegando os 8 últimos
    contacts = Contact.objects.filter( show=True ).order_by('-id')[0:20] 
    # O valores são passados para o template por meio de um dicionário
    context = {
        'contacts': contacts
    }
    return render(
        request, 'contact/index_site.html',
        context
    )

def contact( request, contact_id ):
    # Isso vamos mudar usando o get_object_or_404
    #single_contact = Contact.objects.get( pk = contact_id )
    # Vamos usar o get_object_or_404 para que se o contato não for encontrado, ele retorne um erro 404
    single_contact = get_object_or_404( Contact.objects, pk = contact_id, show = True )

    context = {
        'contact': single_contact
    }
    return render(
        request, 'contact/contact.html',
        context
    )

def index_bootstrap ( requast ):
    contacts = Contact.objects.filter( show=True ).order_by('-id')[0:20]
    context = {
        'contacts': contacts
    }
    return render(
        requast, 'contact/index_bootstrap.html',
        context
    )
    
def contact_bootstrap( request, contact_id ):
    try:
        single_contact = get_object_or_404( Contact.objects, id = contact_id, show = True )
    except Http404:
        single_contact = {
            'first_name': 'Contato ',
            'last_name': 'não encontrado',
            'id' : '-',
            'phone': '-',
            'email': '-',
            'created_date': '-',
            'description': '-',
            'category' : None,
        }

    context = {
        'contact': single_contact
    }
    return render(
        request, 'contact/contact_bootstrap.html',
        context
    )