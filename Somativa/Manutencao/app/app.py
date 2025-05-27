from flask import Flask, jsonify, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
manutencoes = {}

@app.route('/')
def index():
    return render_template("index.html")




def conectar_db():
    return mysql.connector.connect(
        host='mysql_db',
        user='root',
        password='123456',
        database='SkyTech'
    )

def criar_tabela_manutencao():

    conn = None
    cursor = None

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
           CREATE TABLE IF NOT EXISTS manutencao (
            id INT AUTO_INCREMENT PRIMARY KEY,
            aeronave_id INT NOT NULL,
            peca_id INT NOT NULL,
            motivo VARCHAR(255) NOT NULL,
            tipo VARCHAR(100) NOT NULL,
            data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (aeronave_id) REFERENCES aeronaves(id),
            FOREIGN KEY (peca_id) REFERENCES pecas(id)
            )
        """)
        conn.commit()
    except Error as e:
        print("Erro ao criar tabela:", e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()






@app.route('/manutencao', methods=['POST'])
def gerar():
    criar_tabela_manutencao()



    conn = None
    cursor = None
    
    data = request.get_json()
    aeronave_id = data['aeronave_id']
    peca_id = data['peca']
    motivo = data['motivo']
    tipo = data['tipo']


    if not all([aeronave_id, peca_id, motivo, tipo]):
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO manutencao (aeronave_id, peca_id, motivo, tipo) VALUES (%s, %s, %s, %s)",
            (aeronave_id, peca_id, motivo, tipo)
        )
        conn.commit()
        manutencao_id = cursor.lastrowid
        return jsonify({
            'id': manutencao_id,
            'aeronave_id': aeronave_id,
            'peca_id': peca_id,
            'motivo': motivo,
            'tipo': tipo
        }), 201
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
    

@app.route('/manutencao/<int:id>', methods=['GET'])
def buscar(id):
    conn = None
    cursor = None
    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM manutencao WHERE id = %s", (id,))
        manutencao = cursor.fetchone()
        if manutencao:
            return jsonify(manutencao)
        else:
            return jsonify({"erro": "manutencao não encontrada"}), 404
    except Error as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    criar_tabela_manutencao()
    app.run(host='0.0.0.0', port=5001)
