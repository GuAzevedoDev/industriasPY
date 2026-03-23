"""
ATIVIDADE BASEADA NO LIVRO "THINK PYTHON"
Autoria: Downey (2024)

Você está desenvolvendo um sistema simples de controle
de veículos de uma operadora de transporte.

Cada veículo possui:
- placa
- operadora
- ano_fabricacao


Crie uma classe chamada Veiculo.
Ela deve permitir armazenar:

placa
operadora
ano_fabricacao

"""

class Veiculo: #class palavra reservada  Veiculo nome da classe(usamos maiusculo para diferenciar de variaveis) :])
    def __init__(self, placa, operadora, ano_fabricacao): #Esse é o método construtor, ele é chamado automaticamente quando criamos um objeto da classe Veiculo. Ele recebe os parâmetros placa, operadora e ano_fabricacao e os atribui aos atributos do objeto usando self.
        self.placa = placa
        self.operadora = operadora
        self.ano_fabricacao = ano_fabricacao



"""
self
Representa o próprio objeto
É obrigatório em métodos de classe
Permite acessar/modificar os dados do objeto
Pense assim:
self = “este veículo aqui”"""

# Criando objetos
v1 = Veiculo("ABC1234", "Empresa A", 2015)
v2 = Veiculo("XYZ9876", "Empresa B", 2018)
v3 = Veiculo("ABC1234", "Empresa A", 2015)  # duplicado

# Lista
veiculos = [v1, v2, v3]

# Função de exibição
def mostrar_veiculo(v):
    print(f"Placa: {v.placa} | Operadora: {v.operadora} | Ano: {v.ano_fabricacao}")


# Mostrar todos
for v in veiculos:
    mostrar_veiculo(v)


# Verificar duplicidade (placa + operadora)
def verificar_duplicados(lista):
    vistos = set()

    for v in lista:
        chave = (v.placa, v.operadora)

        if chave in vistos:
            print("Duplicado encontrado:", chave)
        else:
            vistos.add(chave)


verificar_duplicados(veiculos)


'''
Atividade: Sistema de Biblioteca
Objetivo

Trabalhar:
Classes
Objetos
Listas
Funções
Regra de negócio (chave composta)


Você está desenvolvendo um sistema simples para controle de livros de uma biblioteca.

Cada livro possui:
titulo
autor
ano_publicacao

Parte 1 — Criando a classe

Crie uma classe chamada Livro com os atributos:
titulo
autor
ano_publicacao

Parte 2 — Criando objetos 
Crie pelo menos 3 livros, sendo que um deles deve ser repetido (mesmo título e autor).

Parte 3 — Lista de livros
Armazene os livros em uma lista e percorra imprimindo todos.

Parte 4 — Função de exibição 
Crie uma função que receba um livro e imprima:
Crie uma função que verifique:
Se existe duplicidade de (titulo + autor)
Se houver, mostrar:
Duplicado encontrado: ('Dom Casmurro', 'Machado de Assis')'''