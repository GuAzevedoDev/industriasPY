from core.services import registrarPeca, retirarPeca,mostrar_banco,sair
import os

def menu():
    while True:
        menu = {
            "1": registrarPeca,
            "2": retirarPeca,
            "3": mostrar_banco,
        }
        os.system('cls')

        print(f"{'='*10}Industria PY{'='*10}\n")
        print("Adicionar peca no estoque [1]\nRetirar peca do estoque [2]\nMostrar estoque completo [3]\n")
        
        opcao = input("Digite o numero da funcao: ")
        funcao = menu.get(opcao)

        if funcao: 
            funcao()
        else:
            print("Digite uma opcao valida\n")
        
        sair()
        

       
