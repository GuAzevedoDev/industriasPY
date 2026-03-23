from core.services import *


def menu():
    print(f"{'='*10}Industria PY{'='*10}\n\n")
    while True:
        menu = {
            "1": registrarPeca,
            "2": retirarPeca
        }
       
        print("Escolha a funcao: \n")
        print("Adicionar peca no estoque [1]\nRetirar peca do estoque [2]\n")
        
        opcao = input("Digite o numero da funcao: ")
        funcao = menu.get(opcao)

        if funcao: 
            funcao()

        else:
            print("Digite uma opcao valida")
