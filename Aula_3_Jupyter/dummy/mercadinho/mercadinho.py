# author: lucas Borguezam
# version: 1.0.1
# data: abr/09/2022
# descryption: Programa que cadastra usuário
# name: mercadinho fatec

from hashlib import sha256 #criptograf
import sys
from this import d
from time import sleep

# menssagem de boas vendas
mensagem = "Olá seja bem vindo a o Mercadinho Fatec"

#Laço para imprimir a menssagem como máquina de escrever
for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    sleep(0.01)
print()

# setando (configurando) as opções do menu
opcoes_de_menu = ["sign in", "sing up", "fale conosco"]
#imprimindo menu de opções
cont = 1
for opcao in opcoes_de_menu :
    print(f"[{cont}] - {opcao}")
    cont+=1 # cont = cont + 1
#pronpt
opcao_digitada = input("Qual opção deseja? ")
#abrindo csv para leitura
with open("db.csv") as arquivo: # open("db.csv")
    print(arquivo.read()) #arquivo.write("test") --cria o arquivo referenciado
    