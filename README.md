
# APITreino

APITreino é um projeto de aprendizado para a criação de uma API utilizando Python, Django e Django Ninja. Este projeto tem como objetivo gerenciar alunos e suas aulas concluídas em um sistema de treinamento.

## Estrutura de Arquivos

A estrutura de arquivos do projeto é a seguinte:

```
APITreino/
├── core/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── api.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── treino/
    ├── __init__.py
    ├── __pycache__/
    ├── admin.py
    ├── api.py
    ├── apps.py
    ├── graduacao.py
    ├── migrations/
    ├── models.py
    ├── schemas.py
    ├── tests.py
    └── views.py
```

### Descrição dos Arquivos

- **core/**: Contém os arquivos principais do projeto Django.
  - `api.py`: Configuração da API utilizando Django Ninja.
  - `asgi.py`: Configuração ASGI para o projeto.
  - `settings.py`: Configurações do projeto Django.
  - `urls.py`: Configuração das URLs do projeto.
  - `wsgi.py`: Configuração WSGI para o projeto.

- **treino/**: Contém os arquivos específicos do aplicativo de treino.
  - `api.py`: Implementação das rotas da API.
  - `apps.py`: Configuração do aplicativo Django.
  - `graduacao.py`: Funções relacionadas à graduação dos alunos.
  - `models.py`: Definição dos modelos do banco de dados.
  - `schemas.py`: Definição dos esquemas utilizados pela API.
  - `tests.py`: Testes do aplicativo.
  - `views.py`: Views do aplicativo (atualmente não utilizadas).

- **db.sqlite3**: Banco de dados SQLite utilizado pelo projeto.
- **manage.py**: Script de gerenciamento do Django.

## Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- Django 5.1.6
- Django Ninja

### Instalação

1. Clone o repositório:

```sh
git clone https://github.com/seu-usuario/APITreino.git
cd APITreino
```

2. Crie um ambiente virtual e ative-o:

```sh
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:

```sh
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:

```sh
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```sh
python manage.py runserver
```

### Endpoints da API

- **POST /api/**: Cria um novo aluno.
- **GET /api/alunos/**: Lista todos os alunos.
- **GET /api/progresso_aluno/**: Obtém o progresso de um aluno específico.
- **POST /api/aula_realizada/**: Marca aulas como realizadas para um aluno.
- **PUT /api/aluno/{aluno_id}**: Atualiza as informações de um aluno.

### Exemplo de Uso

Para criar um novo aluno, envie uma requisição POST para `/api/` com o seguinte corpo:

```json
{
  "nome": "João Silva",
  "email": "joao.silva@example.com",
  "data_nascimento": "2000-01-01",
  "faixa": "B"
}
```

Para listar todos os alunos, envie uma requisição GET para `/api/alunos/`.

Para obter o progresso de um aluno, envie uma requisição GET para `/api/progresso_aluno/` com o parâmetro `email_aluno`.

Para marcar aulas como realizadas, envie uma requisição POST para `/api/aula_realizada/` com o seguinte corpo:

```json
{
  "qtd": 5,
  "email_aluno": "joao.silva@example.com"
}
```

Para atualizar as informações de um aluno, envie uma requisição PUT para `/api/aluno/{aluno_id}` com o corpo contendo os dados atualizados.

## Contribuição

Sinta-se à vontade para contribuir com este projeto enviando pull requests ou abrindo issues.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.




