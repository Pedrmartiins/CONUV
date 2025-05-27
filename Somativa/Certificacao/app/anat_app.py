from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/consultar', methods=['POST'])
def consultar():
    tecnico_id = request.form.get('tecnico_id')
    try:
        response = requests.get(f'http://localhost:5004/verificar_credencial/{tecnico_id}')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
