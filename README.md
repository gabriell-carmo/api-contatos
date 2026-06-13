# 📞 API de Contatos

API REST para gerenciamento de contatos, desenvolvida com Python e Flask.

## 🛠️ Tecnologias

- Python 3
- Flask
- Git & GitHub

## ⚙️ Como rodar localmente

```bash
# Instale o Flask
pip install flask

# Rode o servidor
python app.py
```

O servidor vai rodar em: http://127.0.0.1:5000

## 📋 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /contatos | Lista todos os contatos |
| GET | /contatos/:id | Busca contato por ID |
| POST | /contatos | Cria um novo contato |
| DELETE | /contatos/:id | Remove um contato |

## 📝 Exemplo de uso

**Criar contato:**
```json
POST /contatos
{
    "nome": "Gabriel Carmo",
    "telefone": "17 996569732",
    "email": "gabriellcarmo.dev@gmail.com"
}
```

**Resposta:**
```json
{
    "id": 1,
    "nome": "Gabriel Carmo",
    "telefone": "17 996569732",
    "email": "gabriellcarmo.dev@gmail.com"
}
```