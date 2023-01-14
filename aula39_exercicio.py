"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
nova_string = ''
aux=0
while aux < len(nome):
    nova_string += f"*{nome[aux]}"
    aux += 1
print(nova_string)



#nova_string += '*L*u*i*z* *O*t*á*v*i*o'