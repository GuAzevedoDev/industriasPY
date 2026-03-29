from core.services import registrarPeca, retirarPeca,mostrar_banco,sair,adicionarPeca,entradaFuncionario,mostrarMovimentacoes,estoqueAbaixo
import os

def menu():
    os.system('cls')
    atualFuncionario = entradaFuncionario()
    if atualFuncionario:
        menu = {
            "gerente": {
                "1": ("Registrar peca no estoque", registrarPeca),
                "2": ("Retirar peca do estoque", retirarPeca),
                "3": ("Mostrar estoque completo", mostrar_banco),
                "4": ("Adcionar nova peca", adicionarPeca),
                "5": ("Mostrar movimentacoes", mostrarMovimentacoes),
                "6": ("Alerta de estoque", estoqueAbaixo),
            },
            "vendedor": {
                "1": ("Mostrar estoque completo", mostrar_banco),
                "2": ("Retirar peca do estoque", retirarPeca),
                "3": ("Alerta de estoque", estoqueAbaixo),
            },
            "estoquista": {
                "1": ("Mostrar estoque completo", mostrar_banco),
                "2": ("Registrar peca no estoque", registrarPeca),
                "3": ("Adcionar nova peca", adicionarPeca),
            }
        }
        while True: 
            os.system('cls')
            print(f"{'='*10}Industria PY{'='*10}\n")
            print(f"{atualFuncionario['nome']} // {atualFuncionario['cargo']}\n\n")
            
            menuCerto = menu[atualFuncionario['cargo']]

            for key, (nome,_) in menuCerto.items():
                print(f"{key}: {nome}")
            print("0: Sair")
            opcao = input("\nDigite o numero da funcao: ")
            _,funcao = menuCerto.get(opcao,(None,None))

            if opcao == "0":
                break
            if funcao: 
                funcao(atualFuncionario)
            else:
                print("Digite uma opcao valida\n")
            
        

       
