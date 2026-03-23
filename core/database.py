def lerBanco():
    import json
    caminho = r"H:\industriasPY\data\banco.json"
    with open(caminho,"r", encoding="utf-8") as arquivo: 
        dados = json.load(arquivo)
    return dados
