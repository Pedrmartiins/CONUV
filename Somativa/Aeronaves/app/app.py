from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conectar_db():
    return mysql.connector.connect(
        host='mysql_db',
        user='root',
        password='123456',
        database='SkyTech'
    )

def criar_tabela_aeronaves():
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aeronaves (
                id INT AUTO_INCREMENT PRIMARY KEY,
                modelo VARCHAR(100),
                fabricante VARCHAR(100),
                horas_voo INT
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


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aeronaves', methods=['POST'])
def cadastrar_aeronave():
    data = request.get_json()
    modelo = data.get('modelo')
    fabricante = data.get('fabricante')
    horas_voo = data.get('horas_voo')

    if not all([modelo, fabricante, horas_voo]):
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO aeronaves (modelo, fabricante, horas_voo) VALUES (%s, %s, %s)",
            (modelo, fabricante, horas_voo)
        )
        conn.commit()
        aeronave_id = cursor.lastrowid
        return jsonify({'id': aeronave_id, 'modelo': modelo, 'fabricante': fabricante, 'horas_voo': horas_voo}), 201
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

@app.route('/aeronaves', methods=['GET'])
def listar_aeronaves():

    conn = None
    cursor = None

    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM aeronaves")
        resultado = cursor.fetchall()
        return jsonify(resultado)
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

@app.route('/aeronaves/<int:id>', methods=['GET'])
def obter_aeronave(id):

    conn = None
    cursor = None
    
    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM aeronaves WHERE id = %s", (id,))
        aeronave = cursor.fetchone()
        if aeronave:
            return jsonify(aeronave)
        else:
            return jsonify({'erro': 'Aeronave não encontrada'}), 404
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()




if __name__ == '__main__':
    criar_tabela_aeronaves() 
    app.run(host='0.0.0.0', port=5002)
