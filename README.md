# 📞 API de Contatos

API REST para gerenciamento de contatos, desenvolvida com Python, Flask e SQLite.

## 🛠️ Tecnologias

- Python 3
- Flask
- SQLite
- Git & GitHub
- Postman

## ⚙️ Como rodar localmente

Instale o Flask:
```
pip install flask
```

Rode o servidor:
```
python app.py
```

O servidor vai rodar em: http://127.0.0.1:5000

## 📋 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /contatos | Lista todos os contatos |
| GET | /contatos/:id | Busca contato por ID |
| GET | /contatos?nome=gabriel | Busca contatos por nome |
| GET | /contatos?pagina=1&por_pagina=5 | Listagem paginada |
| POST | /contatos | Cria um novo contato |
| PUT | /contatos/:id | Atualiza um contato |
| DELETE | /contatos/:id | Remove um contato |

## 📝 Exemplo de uso

Criar contato — POST /contatos:
```
{
    "nome": "Gabriel Carmo",
    "telefone": "17 99999-9999",
    "email": "gabriel@email.com"
}
```

Buscar por nome:
```
GET /contatos?nome=gabriel
```

## 🗄️ Banco de Dados

O projeto usa SQLite. Na primeira execução o arquivo contatos.db é criado automaticamente.

Para rodar as migrations:
```
python migration.py
```