from core.services import registrarPeca, retirarPeca,mostrar_banco,sair,adicionarPeca,entradaFuncionario,mostrarMovimentacoes
import os

def menu():
    os.system('cls')
    atualFuncionario = entradaFuncionario()
    if atualFuncionario:
        while True:
            menu = {
                "1": registrarPeca,
                "2": retirarPeca,
                "3": mostrar_banco,
                "4": adicionarPeca,
                "5": mostrarMovimentacoes
            }
            os.system('cls')

            print(f"{'='*10}Industria PY{'='*10}\n")
            print(f"Funcionario: {atualFuncionario['nome']} // {atualFuncionario['cargo']}")
            print("Registrar peca no estoque [1]\nRetirar peca do estoque [2]\nMostrar estoque completo [3]\nAdcionar nova peca [4]\nMostrar movimentacoes [5]\n")
            
            opcao = input("Digite o numero da funcao: ")
            funcao = menu.get(opcao)

            if funcao: 
                funcao(atualFuncionario)
            else:
                print("Digite uma opcao valida\n")
            
        

       
