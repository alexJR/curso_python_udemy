"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
nome_invertido = nome[::-1]

if bool(nome) and bool(idade):
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    if ' ' in nome: 
        print(f"O nome {nome} possui espaço") 
    else:
        print(f"O nome {nome} não possui espaço")
    print(f"O nome {nome} possui {len(nome)} letras")
    print(f"A primeira letra do nome {nome} é '{nome[0]}'")
    print(f"A última letra do nome {nome} é '{nome[-1]}'")
else:
    print("Desculpe, você deixou campos vazios.")
