from core.database import lerBanco
import os

""" Mostrar Banco """

def mostrar_banco():
    pecas = lerBanco()["pecas"]
    print("*******Estoque atual:********")
    for peca in pecas:
        print(f"ID: {peca['id']} // Nome: {peca['peca']}")



""" Sair """

def sair():
    sair = input( '\nPRESSIONE "ENTER" PARA CONTINUAR ' ) 
    if not sair:
        os.system('cls')
    else: 
        exit()
        
    

""" Buscar Peca """

def buscar_peca(pecaBuscada):
    encontrados = []
    pecas = lerBanco()['pecas']
    for peca in pecas:
        if pecaBuscada.lower() in peca['peca'].lower():
            encontrados.append(peca)
           
    if not encontrados:
        print("Peca nao encontrada")
        return None
    
    if len(encontrados) == 1:
        peca = encontrados[0]
        print("Peca encontrada!")
        print(f"ID: {peca['id']}")
        print(f"Peca: {peca['peca']}")
        print(f"Carros compativeis: {peca['veiculos']}")
        print(f"Fabricantes: {peca['fabricante']}")
        return peca

    if len(encontrados) > 1:
        print(f"\n\nForam encontradas {len(encontrados)} pecas que correspondem a sua pesquisa\n")
        for peca in encontrados:
            print(f"ID: {peca['id']}")
            print(f"Peca: {peca['peca']}\n")

        idInput = int(input("Digite o ID da peca escolhida: "))

        for peca in encontrados:
            if idInput == peca['id']:
                print(f"ID: {peca['id']}")
                print(f"Peca: {peca['peca']}")
                print(f"Carros compativeis: {peca['veiculos']}")
                print(f"Fabricantes: {peca['fabricante']}")
                return peca
        else: print("O id digitado nao esta na lista")



""" Registrar Peca """

def registrarPeca():
    pecas = lerBanco()['pecas']
    pecaBuscada = input("Digite a peca que deseja registrar: \n")
    peca = buscar_peca(pecaBuscada)
    if peca in pecas:
        quantidade = int(input("Digite a quantidade: "))
        peca["quantidade"] += quantidade
        print(f"{quantidade} {peca['peca']} adicionadas no estoque")
    # else:
    #     opcao = input("Deseja registrar? (s/n) ")
    #     if opcao.lower() == "s":
    #         adicionarPeca()
    #         print("peca adicionada")
    sair()       

""" Adicionar peca """

# def adicionarPeca(nomePeca,tipo,parte,veiculos,fabricante,data_fabricacao,quantidade):
#     pecas = lerBanco()['pecas']
#     maiorId = len(pecas)
#     atualId = maiorId+1 
#     novaPeca = {"id": atualId, "peca" : nomePeca, "tipo" : tipo, "parte" : parte, "veiculos" : [veiculos],}



# novo_item = {"id": 1, "nome": "Indústria Alpha", "setor": "Mecânica"}
# adicionarAoBanco(novo_item)



""" Retirar Peca """

def retirarPeca():
    pecas = lerBanco()['pecas']
    pecaBuscada = input("Digite a peca que deseja retirar: \n")
    peca = buscar_peca(pecaBuscada)
    quantidade = int(input("Digite a quantidade: "))
    if peca in pecas:
        peca["quantidade"] -= quantidade    
    else:
        peca["quantidade"] = quantidade

    print(quantidade, peca['peca'], "retirado do estoque.")
    sair()



