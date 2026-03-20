# menu





# saida de peca
def retirarPeca(peca, quantidade, preco, dtpreco, tamanho, pais, dtEntrada, usr_entrada, acesso, dt_saida, usr_saida, equipe ):

    if item in estoque:
        estoque_[item] -= quantidade
    else:
        estoque[item] = quantidade

    print(quantidade, item, "retirado do estoque.")

#entrada de peca
def registrarPeca(estoque, item, quantidade):

    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade

    print(quantidade, item, "adicionados ao estoque.")

#procurar por codigo


#procurar por produto

mostrar_estoque()