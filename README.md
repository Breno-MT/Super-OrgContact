# Super OrgContact 
### Sobre o Projeto:
- Desafio realizado para empresa Conecta Nuvem, aonde basicamente é fazer um sistema de lista de contatos, que agrupa pelo domínio os contatos do Google do usuário que fizer o login na plataforma.

### Linguagem de programação utilizada
- Desenvolvida em Python, Flask, Utilizando API do Google People para requisições, MongoDB para salvar usuário logados pelo OAuth do Google.

### Como usar:
- Crie uma venv na raíz do projeto utilizando:
```
python -m venv venv_nome
source venv_name/Scripts/activate - Windows Git Bash
venv_name/bin/activate - Linux
```
- Depois de criado a venv e ativado a mesma, realize o seguinte comando para instalar as dependencias do projeto:
```
python -m pip install -r requirements.txt
```
- Digite no terminal com a venv ativada para criar no MongoDB Atlas a database e sua collection:
```
flask create_collection
```
### Crie uma pasta na src/ chamada database, e adicione o credentials.json, client_secret.json do Google.
- Obs: para pegar ambos arquivos, vá no API & Services do Google e configure lá corretamente conforme a imagem abaixo:
https://imgur.com/a/lhNfdHi

### Depois de configurado tudo perfeitamente, rode o comando abaixo:
```
flask run
```

### Endpoints
- Contacts: contacts/people_api/v1/get_all_connections, Método GET
- Contacts: contacts/people_api/v1/list_10_connections, Método GET
- Users: users/auth/google, Método POST
- Users: users/callback, Método GET
