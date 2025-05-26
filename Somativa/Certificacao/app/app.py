from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
prontuarios = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prontuario', methods=['POST'])
def salvar():
    data = request.get_json()
    id = str(len(prontuarios) + 1)
    prontuarios[id] = data
    return jsonify({"id": id, "prontuario": data}), 201

@app.route('/prontuario/<id>', methods=['GET'])
def buscar(id):
    prontuario = prontuarios.get(id)
    if not prontuario:
        return jsonify({"erro": "Prontuário não encontrado"}), 404
    return jsonify(prontuario)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
