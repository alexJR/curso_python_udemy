""" Cálculadora While"""

valor1 = 0
valor2 = ''
while True:
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")
    valor1 = float(valo1)
    valor2 = float(valo2)
    try:
        
        operador = input("Escolha o Operador: \n [1] SOMA \n [2] SUBTRAÇÃO \n [3] DIVISÃO \n [4] MULTIPLICAÇÃO \n Opção:")
        if operador == '1':
            print("A SOMA dos dois números é: ", valor1 + valor2)
        elif operador == '2':
            print("A SUBTRAÇÃO dos dois números é: ", valor1 - valor2) 
        elif operador == '3':
            print("A DIVISÃO dos dois números é: ", valor1 / valor2) 
        else:
            print("A MULTIPLICAÇÃO dos dois números é: ", valor1 * valor2)
    except:
        print("Favor digitar um número válido") 

        "teste sdsd"
