from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
faturas = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fatura', methods=['POST'])
def gerar():
    data = request.get_json()
    id = str(len(faturas) + 1)
    valor = 100  # Exemplo fixo, substituir com cálculo real
    faturas[id] = {**data, "valor": valor}
    return jsonify({"id": id, "fatura": faturas[id]}), 201

@app.route('/fatura/<id>', methods=['GET'])
def buscar(id):
    fatura = faturas.get(id)
    if not fatura:
        return jsonify({"erro": "Fatura não encontrada"}), 404
    return jsonify(fatura)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
