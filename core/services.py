from core.database import lerBanco,salvarBanco
from datetime import datetime
import os
import pandas as pd
from pandas import json_normalize
from tabulate import tabulate

""" Sair """

def sair():
    sair = input( '\nPRESSIONE "ENTER" PARA CONTINUAR ' ) 
    if not sair:
        os.system('cls')
    else: 
        exit()
        
    

""" Buscar Peca """

def buscar_peca(pecaBuscada,pecas):
    encontrados = []
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



""" Mostrar Banco """

def mostrar_banco(funcionarioAtual):
    if funcionarioAtual['cargo'] in ["gerente","vendedor","estoquista"] :
        banco = lerBanco()
        pecas = banco["pecas"]
        df = json_normalize(pecas)
        pd.set_option('display.max_rows', None)
        print("*******Estoque atual:********")
        print(tabulate(df.values, headers=list(df.columns), tablefmt='fancy_grid'))
    sair()



""" Registrar Peca """

def registrarPeca(funcionarioAtual):
    if funcionarioAtual['cargo'] in ["gerente","vendedor","estoquista"] :
        banco = lerBanco()
        pecas = banco['pecas']
        pecaBuscada = input("Digite a peca que deseja registrar: \n")
        peca = buscar_peca(pecaBuscada,pecas)
        if peca:
            quantidade = int(input("Digite a quantidade: "))
            peca["quantidade"] += quantidade
            salvarBanco(banco)   
            print(quantidade, peca['peca'], "adicionadas com sucesso")
            salvarMovimentacoes("Registro de peca",peca['id'],peca['peca'],quantidade,funcionarioAtual['id'])
        else:
            opcao = input("Deseja registrar? (s/n) ")
            if opcao.lower() == "s":
                adicionarPeca()    
    else: 
        print("Voce nao tem permissao para fazer isso")
    sair()



""" Retirar Peca """

def retirarPeca(funcionarioAtual):
    if funcionarioAtual['cargo'] in ["gerente","vendedor"] :
        banco = lerBanco()
        pecas = banco['pecas']
        pecaBuscada = input("Digite a peca que deseja retirar: \n")
        peca = buscar_peca(pecaBuscada,pecas)
        if peca:
            quantidade = int(input("Digite a quantidade: "))
            if peca['quantidade'] >= quantidade:
                peca["quantidade"] -= quantidade
                salvarBanco(banco)   
                print(quantidade, peca['peca'], "retirado do estoque.")
                salvarMovimentacoes("Retirada de peca",peca['id'],peca['peca'],quantidade,funcionarioAtual['id'])
            else:
                print("Estoque insuficiente")
        else:
            opcao = input("Deseja registrar? (s/n) ")
            if opcao.lower() == "s":
                adicionarPeca(funcionarioAtual)
            else:
                print("Operacao cancelada.\n")
    else: 
        print("Voce nao tem permissao para fazer isso")
    sair()



""" Adicionar peca """

def adicionarPeca(funcionarioAtual):
    if funcionarioAtual['cargo'] in ["gerente","vendedor","estoquista"]:
        banco = lerBanco()
        pecas = banco["pecas"]
        
        atualId = max(peca['id'] for peca in pecas) + 1

        nomePeca = input("Digite o nome da peca: ")
        tipo = input("Digite o tipo da peca (interior/eletronica/externo/mecanica/iluminacao): ")
        parte = input("Digite a parte onde fica a peca: ")
        veiculos = input("Digite os veiculos compativeis: ")
        fabricante = input("Digite o nome do fabricante: ")
        data_fabricacao = input("Digite a data de fabricacao: ")
        quantidade = int(input("Digite a quantidade: "))

        tamanhoClass = {
            "interior": "medio",
            "eletronica": "pequeno",
            "externo": "grande",
            "mecanica": "grande",
            "iluminacao": "medio"
        }
        tamanho = tamanhoClass.get(tipo.lower(), "medio")

        novaPeca = {
            "id": atualId,
            "peca": nomePeca,
            "tipo": tipo,
            "parte": parte,
            "veiculos": veiculos,
            "fabricante": fabricante,
            "data_fabricacao": data_fabricacao,
            "quantidade": quantidade,
            "tamanho": tamanho
        }

        pecas.append(novaPeca)
        salvarBanco(banco)
        print(f"Peca adicionada com sucesso! Classificada como: {tamanho}")
    else:
        print("Voce nao tem permissao para fazer isso")
    sair()



""" Entrada Funcionario """

def entradaFuncionario():
    banco = lerBanco()
    funcionarios = banco['funcionarios']
    escolhido = None
    entradaId = int(input("Digite o ID do seu usuario: "))
    for funcionario in funcionarios:
        if entradaId == funcionario['id']:
            escolhido = funcionario
            break

    if escolhido is None:
        print("Id incorreto,faca login novamente")
        return None 
    
    i = 1
    while i <= 3:
        entradaSenha = input("Digite sua senha: ")
        if entradaSenha == escolhido['senha']:
            print(f"Voce entrou como {escolhido['nome']}")
            return escolhido 
        else:
            if i == 1:
                print("Senha incorreta (Voce tem mais duas tentativas)")
            elif i == 2:
                print("Senha incorreta (Voce tem mais uma tentativa)")
            elif i == 3:
                print("Senha incorreta (Tente fazer login de novo)")

            i += 1
    return None
                        


""" Salvar movimentacao """

def salvarMovimentacoes(nomeFunc, idMovimentada, nomePeca, quantidade, idFuncionario):
    banco = lerBanco()
    movimentacoes = banco['movimentacoes']
    idNovo = max((mov['id'] for mov in movimentacoes), default=0) + 1
    novaMov = {
        "id": idNovo,
        "tipo": nomeFunc,
        "id_peca": idMovimentada,
        "nome_peca": nomePeca,
        "quantidade": quantidade,
        "id_funcionario": idFuncionario,
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    movimentacoes.append(novaMov)
    salvarBanco(banco)



""" Mostrar movimentacoes """

def mostrarMovimentacoes(funcionarioAtual):
    if funcionarioAtual['cargo'] in ["gerente"]:
        banco = lerBanco()
        movimentacoes = banco['movimentacoes']
        df = json_normalize(movimentacoes)
        pd.set_option('display.max_rows', None)
        print(tabulate(df.values, headers=list(df.columns), tablefmt='fancy_grid'))
        sair()
    else:
        print("Voce nao tem permissao para fazer isso")



""" Estoque abaixo """

def estoqueAbaixo(funcionarioAtual):
    limite = int(input("Exibir peças com estoque abaixo de: "))
    banco = lerBanco()
    pecas = banco["pecas"]
    df = json_normalize(pecas)
    pd.set_option('display.max_rows', None)
    resultado = df[df['quantidade'] < limite]
    print(tabulate(resultado.values, headers=list(resultado.columns), tablefmt='fancy_grid'))
    sair()