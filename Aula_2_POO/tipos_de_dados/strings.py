import string

#aspas duplas
"Todos os sapos pulam os rios"

#aspas simples
'nem todos os rios são quentes'

#aspas triplas duplas: permite quebra de linha
"""mas todos os quentes são rios"""

#aspas triplas símples: permite quebra de linha
'''e todos os sapos são anfíbios'''

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

#print (f"olá, {nome.title()}, você tem: {idade} anos.")

print("olá, {}, você tem: {} anos.".format(nome.title(), idade))

#estrutura de repetição
