from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
consultas = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/consulta', methods=['GET'])
def listar_todas():
    return jsonify(consultas)


@app.route('/consulta', methods=['POST'])
def agendar():
    data = request.get_json()
    id = str(len(consultas) + 1)
    consultas[id] = data
    return jsonify({"id": id, "consulta": data}), 201

@app.route('/consulta/<id>', methods=['GET'])
def buscar(id):
    consulta = consultas.get(id)
    if not consulta:
        return jsonify({"erro": "Consulta não encontrada"}), 404
    return jsonify(consulta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
