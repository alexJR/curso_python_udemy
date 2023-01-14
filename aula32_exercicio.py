"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_inteiro = input("Digite um valor inteiro: ")

try:
    num_inteiro = int(num_inteiro)
    num_par = num_inteiro % 2
    if num_par == 0:
        print(f"{num_par} é um número PAR")
    else:
        print(f"{num_par} é um número ÍMPAR")
except:
    input("Esse não é um valor inteiro!")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora atual: ")

try:
    hora_int = int(hora)
    if hora_int <= 11:
        print("Bom dia")
    elif hora_int <= 17:
        print("Boa tarde")
    else:
        print("Boa noite")
except:
    input("Favor digitar somente a hora!")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("Digite o seu primeiro nome: ")

qtd_caracteres_nome = len(primeiro_nome)

if qtd_caracteres_nome > 6:
    print("Seu nome é muito grande")
elif qtd_caracteres_nome >= 5:
    print("Seu nome é normal")
else:
    print("Seu nome é curto")
