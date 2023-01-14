"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 102  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


if velocidade > RADAR_1:
    print("Velocidade acima do permitido")
    if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
        print(f"Você acaba de ser multado, velocidade permitida do radar {RADAR_1}, velocidade que passou {velocidade}")
    else:
        print("Fique de olho nos radares!")
else:
    print("Você está abaixo da velocidade máxima permitida, continue assim!") 