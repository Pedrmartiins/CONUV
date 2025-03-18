from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

db_config ={
    'host': 'db',
    'user': 'root',
    'password': 'password',
    'database': 'cadastro_db'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    data = request.json
    nome = data['nome']
    email = data['email']


    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s,%s)", (nome, email))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Cadastro realizado com sucesso!"}), 200
    except Exception as e:

        return jsonify({"message": str(e)}), 500

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)