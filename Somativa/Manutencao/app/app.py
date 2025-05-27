from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
manutencoes = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/manutencao', methods=['POST'])
def gerar():
    data = request.get_json()
    id = str(len(manutencoes) + 1)
    valor = 100  # Exemplo fixo, substituir com cálculo real
    manutencoes[id] = {**data, "valor": valor}
    return jsonify({"id": id, "manutencao": manutencoes[id]}), 201

@app.route('/manutencao/<id>', methods=['GET'])
def buscar(id):
    manutencao = manutencoes.get(id)
    if not manutencao:
        return jsonify({"erro": "manutencao não encontrada"}), 404
    return jsonify(manutencao)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
