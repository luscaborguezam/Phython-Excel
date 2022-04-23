# lendo(read) banco de dados
from nbformat import write


def ler_banco():#toda função é um verbo
    """Essa função lê um banco de dados"""
    with open("estoque.csv", "r") as file: 
        #print(file.read().split()[0])
        dados_do_banco = file.read() # pegando os dados do banco em formato de texto
        dados_do_estoque = dados_do_banco.split("\n") # quebrando em linhas
        menu = dados_do_estoque[0].split(",")
        quantidade_no_estoque = dados_do_estoque[1].split(",")
        return menu, quantidade_no_estoque

#menu, quantidade = ler_banco()    
intens_menu = ler_banco()[0]
estoque_menu = ler_banco()[1]

print("\033[1;32mFaça seu pedido:\033[m ")
# listando o menu
for posicao, item in enumerate(intens_menu):
     print(f"[{posicao + 1}] - {item}") 
#interação do usuário
pedido = int(input(">>> ")) # retorna texto
print(f"\033[1;36m{pedido}\033[m")    

tamanho_menu = len(intens_menu) #len retorna int


if pedido > tamanho_menu or pedido < 1:
    print("\033[1;31mOpção inválida\033[m")
#tirando a máscara do input + 1    
pedido = pedido - 1 #pedido -=1
#fazendo subtração no estoque de acordo com o pedido
estoque_menu[pedido] = str(int(estoque_menu[pedido]) - 1)
#salvando a alteração
with open("estoque.csv", 'w') as file:
    file.write(",".join(intens_menu))
    file.write("\n")
    file.write(",".join(estoque_menu))
#mostrando a variavel alterada
print(estoque_menu)
# Abrindo/criando arquivo
with open("estoque.csv", "a") as file: 
    #file.write("OUTRA COISA\n")
    #dump("texto")
    pass
