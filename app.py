from flask import Flask, jsonify, request
import pandas as pd
import json

app = Flask(__name__)


# Abrindo o arquivo JSON
with open('dados.json', 'r') as arquivo:
    # Carregando os dados do arquivo JSON
    users = json.load(arquivo)

# Got a users list
@app.route('/users', methods=["GET"])
def list_users():
    return jsonify(users)


# Got a user by id
@app.route('/users/<int:id>', methods=["GET"])
def list_users_id(id):
    for user in users:
        if user.get("id") == id:
            return jsonify(user)
        
@app.route('/users/<int:id>', methods = ['PUT'])
def edita_user(id):
    user_alterado = request.get_json()
    for indice, user in enumerate(users):
        if user.get('id') == id:
            users[indice].update(user_alterado)
            return jsonify(users[indice])

        
@app.route('/users/<int:id>', methods = ['DELETE'])
def deleta_user(id):
    for indice, user in enumerate(users):
        if user.get("id") == id:
            del users[indice]


app.run(port=5000, host="localhost", debug=True)

