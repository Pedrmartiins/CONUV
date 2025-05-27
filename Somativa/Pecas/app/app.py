from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Função para conectar ao banco
def conectar_db():
    return mysql.connector.connect(
        host='mysql_db',
        user='root',
        password='123456',
        database='SkyTech'
    )
    print("Conexão com banco estabelecida")
    

# Criação da tabela de peças
def criar_tabela_pecas():
    conn = None
    cursor = None
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pecas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            quantidade INT NOT NULL DEFAULT 0
            )
        """)
        conn.commit()
    except Error as e:
        print("Erro ao criar tabela de peças:", e)
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()

# Página principal com HTML
@app.route('/')
def pagina_pecas():
    return render_template("index.html")

# API para listar peças
@app.route('/api/pecas', methods=['GET'])
def listar_pecas():
    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pecas")
        pecas = cursor.fetchall()
        return jsonify(pecas)
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()

# API para cadastrar nova peça
@app.route('/api/pecas', methods=['POST'])
def cadastrar_peca():
    data = request.get_json()
    nome = data.get('nome')
    quantidade = data.get('quantidade', 0)

    if not nome:
        return jsonify({'erro': 'Nome é obrigatório'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pecas (nome, quantidade) VALUES (%s, %s)", (nome, quantidade))
        conn.commit()
        return jsonify({'mensagem': 'Peça cadastrada com sucesso'}), 201
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()

# API para adicionar mais peças
@app.route('/api/pecas/<int:id>/adicionar', methods=['PUT'])
def adicionar_quantidade(id):
    data = request.get_json()
    adicional = data.get('quantidade')

    if adicional is None:
        return jsonify({'erro': 'Informe a quantidade'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE pecas SET quantidade = quantidade + %s WHERE id = %s", (adicional, id))
        conn.commit()
        return jsonify({'mensagem': 'Quantidade atualizada'}), 200
    except Error as e:
        return jsonify({'erro': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()

# Inicialização
if __name__ == '__main__':
    criar_tabela_pecas()
    app.run(host='0.0.0.0', port=5003, debug=True)
