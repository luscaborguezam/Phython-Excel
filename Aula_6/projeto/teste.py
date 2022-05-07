# Sempre em um prejeto phython criar 2 arquivos importantes
# venv (hambiente virtual) gitignore (github ignora)
# criando venv(Terminal cmd powershell): phython -m venv venv
# criando gitignore: Criar arquivo com o nome de ".gitignore"
# entrando no usuário venv do cmd: venv/scripts/activate
import csv

from flask import Flask
import requests
from http import HTTPStatus

# para fazer o python rodar na internet(FLASCK):

app = Flask(__name__) # controle de erro

#@app.get("/<string:nome>")
# def home(nome):
#     #return f"<h1>{nome}</h1>", HTTPStatus.OK
#     if nome.lower() != "cavalo":
#         return {"msg": f"O valor {nome} que você passou não é válido"}, HTTPStatus.BAD_REQUEST
#     else:
#         return {"msg": "Seja bem-vindo ao clã. Cavalos Codificadores"}

# Endpoint

#READ
@app.get("/get_dados")
def get_info():
    """Essa função lê banco de dados de informações do cavalo"""
    with open("db.csv") as arquivo:
        arquivo_lido = csv.reader(arquivo, delimiter = ',')
        linhas = []
        for linha in arquivo_lido:
            linhas.append(linha)

    return {"dados": linhas}
# UPDATE/Create
@app.get("/")
def salve_info():
    """Essa função atualiza o banco de dados"""
    pass

app.run(port=5050) # em caso de not fauld

# pip install python-dotenv