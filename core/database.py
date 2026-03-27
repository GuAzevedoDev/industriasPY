import json
from pathlib import Path
 
 
def lerBanco():
    pasta_raiz = Path(__file__).parent.parent
    caminho = pasta_raiz / "data" / "banco.json"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados
 
 
def salvarBanco(dados):
    pasta_raiz = Path(__file__).parent.parent
    caminho = pasta_raiz / "data" / "banco.json"
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
 