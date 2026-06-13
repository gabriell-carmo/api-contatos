from flask import Flask, jsonify, request

app = Flask(__name__)

contatos = []

@app.route('/contatos', methods=['GET'])
def listar():
    return jsonify(contatos)

@app.route('/contatos/<int:id>', methods=['GET'])
def buscar(id):
    contato = next((c for c in contatos if c['id'] == id), None)
    if contato:
        return jsonify(contato)
    return jsonify({'erro': 'Contato não encontrado'}), 404

@app.route('/contatos', methods=['POST'])
def criar():
    dados = request.get_json()
    if not dados or 'nome' not in dados:
        return jsonify({'erro': "Campo 'nome' obrigatório"}), 400
    contato = {
        'id': len(contatos) + 1,
        'nome': dados['nome'],
        'telefone': dados.get('telefone', ''),
        'email': dados.get('email', '')
    }
    contatos.append(contato)
    return jsonify(contato), 201

@app.route('/contatos/<int:id>', methods=['DELETE'])
def deletar(id):
    global contatos
    contato = next((c for c in contatos if c['id'] == id), None)
    if not contato:
        return jsonify({'erro': 'Contato não encontrado'}), 404
    contatos = [c for c in contatos if c['id'] != id]
    return jsonify({'mensagem': 'Contato deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)