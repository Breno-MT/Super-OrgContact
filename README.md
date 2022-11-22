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
