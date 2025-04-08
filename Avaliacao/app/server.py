from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import requests
import mysql.connector

app = Flask(__name__, static_folder="static", template_folder="templates")


CORS(app)

API_KEY = "WBIM6DC9QE6QIFNM"
URL = f"https://api.thingspeak.com/update?api_key=WBIM6DC9QE6QIFNM&field1=0"
api_key = "https://api.thingspeak.com/update?api_key=WBIM6DC9QE6QIFNM&field1=0"

def enviar_dados(temp, umi, pres):
    url = f"https://api.thingspeak.com/update?api_key=WBIM6DC9QE6QIFNM&field1={temp}&field2={umi}&field3={pres}"
    resposta = requests.get(url)  
def salvar(temperatura, umidade, pressao):
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '123456',
        'database': 'monitoramento'
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO dados (temperatura, umidade, pressao) 
            VALUES (%s, %s, %s)
        """, (temperatura, umidade, pressao))
        conn.commit()

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print(f"Erro no banco de dados: {e}")
        return False
    return True

def get_sensor_data():
    temp = round(random.uniform(20, 80), 2)
    umi = round(random.uniform(30, 90), 2)
    pres = round(random.uniform(900, 1100), 2)

    enviar_dados(temp, umi, pres)

    salvar(temp, umi, pres)

    return {
        "temperatura": temp,
        "umidade": umi,
        "pressao": pres
    }



if __name__=='__main__':
    app.run(debug=True)