from flask import Flask, make_response, jsonify, request
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='db_creator',
    password='Cr34t0r',
    database='db_carros'
)


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():
    
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM tb_carros;')
    carros = list()
    for carro in cursor.fetchall():
        carros.append(
            {
                'id':carro[0],
                'marca':carro[1],
                'modelo':carro[2],
                'ano':carro[3]
            }
        )
    return make_response(
        jsonify(
            mensagem='Lista de carros',
            dados=carros
        )
    )


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    
    cursor = mydb.cursor()
    
    sql = f"INSERT INTO tb_carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
    cursor.execute(sql)
    mydb.commit()
    
    return make_response(
        jsonify(
            mensagem='carro cadastrado com sucesso',
            dados=carro
        )
    )


app.run()
