from django.shortcuts import render # type: ignore

# agora vamos importar o modelo Contact para que possamos exibir os dados na página
from contact.models import Contact
# Create your views here.
def index(request):
    # Recebendo todos os contatos que temos no banco de dados e ordenando pelo id de forma decrescente
    #contacts = Contact.objects.all().order_by('-id')
    # filtrando os contatos que estão marcados como show=True, e pegando os 8 últimos
    contacts = Contact.objects.filter( show=True).order_by('-id')[0:20] 
    # O valores são passados para o template por meio de um dicionário
    context = {
        'contacts': contacts
    }
    return render(
        request, 'contact/index_site.html',
        context
    )

def contact( request, contact_id ):

    single_contact = Contact.objects.get( pk = contact_id )

    context = {
        'contact': single_contact
    }
    return render(
        request, 'contact/contact.html',
        context
    )