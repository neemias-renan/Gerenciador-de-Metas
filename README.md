# Focus - Gerenciador de Metas

A plataforma (Focus) surgiu em 2021 com o objetivo de auxiliar o usuário a administrar suas metas. O projeto é desenvolvido pelos estudantes Neemias Renan, Vitória Raquel e Sthefany Lima.

## Como instalar:

Use um ambiente virtual para fazer as instalações que serão utilizadas na aplicação:

Na pasta do projeto instale o ambiente virtual:

```sh
$ pip install virtualenv
```
em seguida inicialize o ambiente virtual digite:
```sh
$ virtualenv -p python3 venv
```

Para ativar o ambiente virtual:

No Windows:

$ cd venv\Script\  
  em seguida digite: 
$ activate
```

Volte para a pasta inicial do projeto, e finalmente, instale a lista de pacotes da aplicação:

```sh
$ pip3 install -r requirements.txt
```
## Configurando o projeto

Atualize o banco de dados:

```sh
$ py run.py db init
$ py run.py db migrate
$ py run.py db upgrade
```

Para rodar a aplicação utilize o comando:

```sh
$ py run.py runserver
```

Acesse no seu navegador o seguinte endereço abaixo:

```sh
http://localhost:5000/
```
