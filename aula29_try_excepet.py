valor_str = input("Digite o número para calcularmos o dobro do valor: ")
7


try:
    valor_float = float(valor_str)
    print("Cálculo: ", valor_float * 2)
except:
    print(f"Favor digitar um número válido, valor '{valor_str}', não é um válor válido!")


