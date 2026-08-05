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

livros = carregar_livros()

def cadastrar_livro(lista_livros, titulo, autor, ano, isbn):
# Monta um dicionário com os dados do livro e adiciona à lista. Devolve a lista já atualizada.
    
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponivel"
    }
    lista_livros.append(novo_livro)
    return lista_livros

def listar_livros(lista_livros):
# Mostra os livros da lista no terminal, formatado. Se não tiver nenhum, avisa o usuário.
    
    if not lista_livros:
        print("Nenhum livro cadastrado.\n")
        return

    for livro in lista_livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor : {livro['autor']}")
        print(f"Ano   : {livro['ano']}")
        print(f"ISBN  : {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("--------------------------------\n")
        
def buscar_livros(lista_livros, termo, campo):
# Busca na lista os livros que título ou autor bate com o termo digitado. Se não achar nada, devolve lista vazia mesmo
    
    termo = termo.lower()
    resultado = []

    for livro in lista_livros:
        if termo in livro[campo].lower():
            resultado.append(livro)

    return resultado
        
        