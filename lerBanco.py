def lerBanco():
    import json
    caminho = r"C:\Users\Gustavo\Documents\Python\industriasPY\banco.json"
    with open(caminho,"r", encoding="utf-8") as arquivo: 
        dados = json.load(arquivo)
    return dados



        