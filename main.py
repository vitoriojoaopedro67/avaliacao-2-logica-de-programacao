# ---------- Configuração ----------

import csv
import os

ARQUIVO_CSV = "livros.csv"
# Arquivo utilizado para armazenar os livros cadastrados

CAMPOS = ["titulo", "autor", "ano", "isbn", "status"]
# Função para cadastrar um novo livro


# ---------- Carregar e Salvar dados dos Livros ----------

def carregar_livros():
# Lê o CSV com os livros. Se o arquivo ainda não existe, começamos com uma lista vazia mesmo.

    lista_livros = []

    if not os.path.exists(ARQUIVO_CSV):
        return lista_livros

    with open(ARQUIVO_CSV, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista_livros.append(linha)

    return lista_livros

livros = carregar_livros()


# ---------- Cadastro dos Livros ----------

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


# ---------- Listagem dos Livros ----------

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
 

# ---------- Busca dos Livros ----------

def buscar_livros(lista_livros, termo, campo):
# Busca na lista os livros que título ou autor bate com o termo digitado. Se não achar nada, devolve lista vazia mesmo
    
    termo = termo.lower()
    resultado = []

    for livro in lista_livros:
        if termo in livro[campo].lower():
            resultado.append(livro)

    return resultado
        

# ---------- Empréstimo e Devolução dos Livros ----------

def emprestar_livro(lista_livros, isbn):
# Procura o livro pelo ISBN e, se estiver disponível, marca como "emprestado". Devolve uma mensagem contando o que aconteceu.
    
    for livro in lista_livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "emprestado":
                return "Este livro já está emprestado."
            livro["status"] = "emprestado"
            return "Empréstimo registrado com sucesso."

    return "Livro não encontrado."  

def devolver_livro(lista_livros, isbn):
# Procura o livro pelo ISBN e, se estiver emprestado, marca como "disponível" de volta. Devolve uma mensagem contando o que aconteceu.
    
    for livro in lista_livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "disponivel":
                return "Este livro já está disponível."
            livro["status"] = "disponivel"
            return "Devolução registrada com sucesso."

    return "Livro não encontrado."


# ---------- Ordenação dos Livros ----------

def ordenar_livros(lista_livros, campo):
# Ordena os livros pelo campo escolhido (titulo, autor ou ano) e devolve uma lista nova, sem mexer na original.
    
    if campo not in ("titulo", "autor", "ano"):
        return lista_livros

    return sorted(lista_livros, key=lambda livro: livro[campo])


# ---------- Função para salvar os livros no CSV ----------

def salvar_livros(lista_livros):
# Salva a lista de livros no CSV, sobrescrevendo o que tinha antes.
    
    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for livro in lista_livros:
            escritor.writerow(livro)
     
     
# ---------- Função principal e Menu do Sistema ----------
     
def exibir_menu():
#Imprime as opções do menu principal.

    print("\n===== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA =====")
    print("1. Cadastrar livro")
    print("2. Listar todos os livros")
    print("3. Buscar algum livro")
    print("4. Ordenar alguns livros")
    print("5. Emprestar algum livro")
    print("6. Devolver algum livro")
    print("0. Sair")
    print("===================================================")


def main():
# Tem como função manter o menu rodando até o usuário decidir sair.

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            ano = input("Ano: ").strip()
            isbn = input("ISBN: ").strip()
            cadastrar_livro(livros, titulo, autor, ano, isbn)
            salvar_livros(livros)
            print("Parabéns! Livro cadastrado com sucesso!")

        elif opcao == "2":
            listar_livros(livros)

        elif opcao == "3":
            campo = input("Buscar por (titulo/autor): ").strip().lower()
            termo = input("Digite o termo de busca: ").strip()
            encontrados = buscar_livros(livros, termo, campo)
            listar_livros(encontrados)

        elif opcao == "4":
            campo = input("Ordenar por (titulo/autor/ano): ").strip().lower()
            ordenados = ordenar_livros(livros, campo)
            listar_livros(ordenados)

        elif opcao == "5":
            isbn = input("ISBN do livro a emprestar: ").strip()
            mensagem = emprestar_livro(livros, isbn)
            salvar_livros(livros)
            print(mensagem)

        elif opcao == "6":
            isbn = input("ISBN do livro a devolver: ").strip()
            mensagem = devolver_livro(livros, isbn)
            salvar_livros(livros)
            print(mensagem)

        elif opcao == "0":
            print("Encerrando o sistema. Obrigado por utilizar! Até logo!")
            print("Programa feito por João Pedro Costa Vitório")
            break

        else:
            print("Opção inválida. Tente novamente!")


main()       
