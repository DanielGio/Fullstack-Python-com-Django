# Fullstack Python com Django

Fullstack Python com Django 20261005\_1836



PACOTE BOOTSTRAP - projeto Fullstack Python com Django

========================================================



As pastas deste zip seguem a estrutura do seu projeto. Copie cada arquivo

para o mesmo caminho, substituindo o que já existe (faça um commit antes!).



ARQUIVOS NOVOS

&#x20; cadastro/templatetags/\_\_init\_\_.py            (arquivo vazio)

&#x20; cadastro/templatetags/bootstrap\_extras.py

&#x20; cadastro/templates/cadastro/\_form.html



ARQUIVOS QUE SUBSTITUEM OS SEUS

&#x20; cadastro/templates/cadastro/base.html

&#x20; cadastro/templates/cadastro/index.html

&#x20; cadastro/templates/cadastro/detalhes.html

&#x20; cadastro/templates/cadastro/adicionar.html

&#x20; cadastro/templates/cadastro/contato.html

&#x20; cadastro/templates/cadastro/deletar.html

&#x20; cadastro/templates/registration/login.html

&#x20; cadastro/static/cadastro/style.css

&#x20; cadastro/views.py

&#x20; core/urls.py



UMA ALTERAÇÃO MANUAL em core/settings.py (acrescente no fim do arquivo):



&#x20; from django.contrib.messages import constants as message\_constants



&#x20; MESSAGE\_TAGS = {message\_constants.ERROR: 'danger'}



&#x20; (O Django chama o erro de "error" e o Bootstrap espera "danger".)



TAMBÉM NO settings.py, deixe só UMA vez cada uma destas linhas:



&#x20; LOGIN\_URL = 'login'

&#x20; LOGIN\_REDIRECT\_URL = 'index'

&#x20; LOGOUT\_REDIRECT\_URL = 'index'



NÃO MEXA em: models.py, forms.py, admin.py, cadastro/urls.py.

&#x20; (Os templates usam os nomes de rota index, contato, adicionar, detalhes,

&#x20; editar, deletar, login e logout. Confira que o seu cadastro/urls.py tem

&#x20; detalhes, editar e deletar com esses nomes.)



DEPOIS DE COPIAR

&#x20; 1. Pare o servidor (CTRL+C) e rode de novo. Isso é obrigatório por causa da

&#x20;    pasta templatetags, que o Django só descobre ao iniciar.

&#x20; 2. No navegador, aperte CTRL+F5.

&#x20; 3. Teste: Início, Adicionar, Contato, Entrar, editar e deletar uma pessoa.



O Bootstrap vem de CDN (jsdelivr), então precisa de internet para carregar.



