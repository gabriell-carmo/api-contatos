from flask import Flask, jsonify, request
from database import get_db, close_db, init_db

app = Flask(__name__)

app.teardown_appcontext(close_db)

@app.route('/contatos', methods=['GET'])
def listar():
    db = get_db()
    nome = request.args.get('nome', '')
    pagina = int(request.args.get('pagina', 1))
    por_pagina = int(request.args.get('por_pagina', 5))
    offset = (pagina - 1) * por_pagina

    if nome:
        contatos = db.execute(
            'SELECT * FROM contatos WHERE nome LIKE ? LIMIT ? OFFSET ?',
            (f'%{nome}%', por_pagina, offset)
        ).fetchall()
    else:
        contatos = db.execute(
            'SELECT * FROM contatos LIMIT ? OFFSET ?',
            (por_pagina, offset)
        ).fetchall()

    return jsonify([dict(c) for c in contatos])

@app.route('/contatos/<int:id>', methods=['GET'])
def buscar(id):
    db = get_db()
    contato = db.execute('SELECT * FROM contatos WHERE id = ?', (id,)).fetchone()
    if contato:
        return jsonify(dict(contato))
    return jsonify({'erro': 'Contato não encontrado'}), 404

@app.route('/contatos', methods=['POST'])
def criar():
    dados = request.get_json()
    if not dados or 'nome' not in dados:
        return jsonify({'erro': "Campo 'nome' obrigatório"}), 400
    db = get_db()
    db.execute('INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)',
               (dados['nome'], dados.get('telefone', ''), dados.get('email', '')))
    db.commit()
    return jsonify({'mensagem': 'Contato criado com sucesso!'}), 201

@app.route('/contatos/<int:id>', methods=['PUT'])
def atualizar(id):
    db = get_db()
    contato = db.execute('SELECT * FROM contatos WHERE id = ?', (id,)).fetchone()
    if not contato:
        return jsonify({'erro': 'Contato não encontrado'}), 404
    dados = request.get_json()
    nome = dados.get('nome', contato['nome'])
    telefone = dados.get('telefone', contato['telefone'])
    email = dados.get('email', contato['email'])
    db.execute('UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?',
               (nome, telefone, email, id))
    db.commit()
    return jsonify({'mensagem': 'Contato atualizado com sucesso!'})

@app.route('/contatos/<int:id>', methods=['DELETE'])
def deletar(id):
    db = get_db()
    contato = db.execute('SELECT * FROM contatos WHERE id = ?', (id,)).fetchone()
    if not contato:
        return jsonify({'erro': 'Contato não encontrado'}), 404
    db.execute('DELETE FROM contatos WHERE id = ?', (id,))
    db.commit()
    return jsonify({'mensagem': 'Contato deletado com sucesso!'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)