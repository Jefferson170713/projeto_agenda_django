from django.shortcuts import render

# agora vamos importar o modelo Contact para que possamos exibir os dados na página
from contact.models import Contact
# Create your views here.
def index(request):
    # Recebendo todos os contatos que temos no banco de dados
    contacts = Contact.objects.all()
    # O valores são passados para o template por meio de um dicionário
    context = {
        'contacts': contacts
    }
    return render(
        request, 'contact/index_site.html',
        context
        )