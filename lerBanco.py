

def lerBanco():
    import json
    caminho = r"H:\py\projetopy\bancoDeDados.json"
    with open(caminho,"r", encoding="utf-8") as arquivo: 
        dados = json.load(arquivo)

    print(dados)