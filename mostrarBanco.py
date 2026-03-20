def mostrar_estoque():

    lerB = lerbanco.lerBanco()
    print("*******Estoque atual:********")
for codigo, info in lerBanco().items():
    print(f"Código: {codigo}")
    print(f"  Peça: {info['peca']}")
    print("-" * 30)
    print(f"  Qtd: {info['quantidade']}  Preço: R$ {info['preco']}  data: {info['dt_preco']} tamanho: {info['tamanho']} tamanho: {info['tamanho']} ")