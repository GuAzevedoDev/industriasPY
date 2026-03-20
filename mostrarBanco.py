from lerBanco import lerBanco

def mostrar_banco():
    pecas = lerBanco()["pecas"]
    print("*******Estoque atual:********")
    for peca in pecas:
        chave = peca["id"]
        peca = peca["peca"]
        print(f"ID: {chave}")
        print(f"Peca: {peca}")


def buscar_peca():
    pecas = lerBanco()["pecas"]
    pecaBuscada = "Modulo telemetria TX/RX"
    for peca in pecas:
        if pecaBuscada == peca["peca"]:
            chave = peca["id"]
            peca = peca["peca"]
            print(f"ID: {chave}")
            print(f"Peca: {peca}")

            
    
