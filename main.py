import csv 
import os

ARQUIVO_CSV = "livros.csv"
# Arquivo utilizado para armazenar os livros cadastrados

CAMPOS = ["titulo", "autor", "ano", "isbn", "status"]
# Função para cadastrar um novo livro

def carregar_livros():
# Lê o CSV com os livros. Se o arquivo ainda não existe, começamos com uma lista vazia mesmo.

    if not os.path.exists(ARQUIVO_CSV):
        return lista_livros

    with open(ARQUIVO_CSV, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista_livros.append(linha)

    return lista_livros
