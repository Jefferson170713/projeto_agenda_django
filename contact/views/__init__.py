# Esse arquivo não existe natutalmente no python, por isso precismaos criar
# depois de criar o arquivo, precisamos deletar o arquivo view.py que foi criado automaticamente
# passamos primeiro o que estava dentro do arquivo views.py para o arquivo contact_views.py ou qualquer outro arquivo.
# Mas antes claro, criamos o arquivo __init__.py e importamos as views do arquivo contact_views.py
# pronto, nosso projeto está organizado por pacotes e subpacotes
# sempre que criarmos um nova views ou models, precisamos importar no arquivo __init__.py

#from .contact_views import *
from contact.views.contact_views import *