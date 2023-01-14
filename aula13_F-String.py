nome = 'Alex Rampanelli'
altura = 1.84
peso = 84

## Cálculo do IMC: peso / (altura * altura)

imc = peso / (altura * altura)


resultado = f"A pessoa de nome {nome} possui um IMC de {imc:.2f}"

print("SEM F-STRING:", "A pessoa de nome ", nome, "pessui um IMC de ", imc)
print(f"COM F-STRING: {resultado}")