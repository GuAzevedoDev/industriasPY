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
    encontrados = []
    pecas = lerBanco()['pecas']
    for peca in pecas:
        if pecaBuscada.lower() in peca['peca'].lower():
            encontrados.append(peca)
           
    if not encontrados:
        print("Peca nao encontrada")
        return None
    
    if len(encontrados) == 1:
        print("Peca encontrada!")
        print(f"ID: {peca['id']}")
        print(f"Peca: {peca['peca']}\n")
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
                print(f"Peca: {peca['peca']}\n")
                return peca['peca']
        else: print("O id digitado nao esta na lista")
        
buscar_peca("radio")



                     

    


