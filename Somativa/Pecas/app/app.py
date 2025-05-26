from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# DICIONÁRIO EM MEMÓRIA PARA ARMAZENAMENTO TEMPORÁRIO
# Substitua por conexão a banco de dados se necessário.
registros = {}

@app.route('/')
def index():
    return render_template("index.html")

# ENDPOINT PARA CADASTRO
@app.route('/paciente', methods=['POST'])
def cadastrar():
    data = request.get_json()
    novo_id = str(len(registros) + 1)
    registros[novo_id] = data
    return jsonify({"id": novo_id, "dados": data}), 201

# ENDPOINT PARA CONSULTAR REGISTRO POR ID
@app.route('/paciente/<id>', methods=['GET'])
def consultar(id):
    dado = registros.get(id)
    if not dado:
        return jsonify({"erro": "Registro não encontrado"}), 404
    return jsonify(dado)

# INICIALIZAÇÃO DO SERVIDOR
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Altere a porta aqui para outros serviços (ex: 5002)
