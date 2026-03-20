from lerBanco import lerBanco

def mostrar_banco():
    pecas = lerBanco()["pecas"]
    print("*******Estoque atual:********")
    for peca in pecas:
        chave = peca["id"]
        peca = peca["peca"]
        print(f"ID: {chave}")
        print(f"Peca: {peca}")



def buscar_peca(pecaBuscada):
    encontrada = False
    encontrados = []
    pecas = lerBanco()['pecas']
    for peca in pecas:
        if pecaBuscada.lower() in peca['peca'].lower():
            encontrada = True
            encontrados.append(peca['id'])
            print(f"ID: {peca['id']}")
            print(f"Peca: {peca['peca']}\n")
    if len(encontrados) > 1:
        print(f"\n\nForam encontradas {len(encontrados)} pecas que correspondem a sua pesquisa\n")
        idInput = int(input("Digite o id da peca escolhida: "))
        if idInput in encontrados:
            for peca in pecas:
                if idInput == peca['id']:
                    print(f"ID: {peca['id']}")
                    print(f"Peca: {peca['peca']}\n")
        else: print("O id digitado nao esta na lista")

    if not encontrada:
        print("Peca nao encontrada")   
        
buscar_peca("Volante esportivo")



                     

    


