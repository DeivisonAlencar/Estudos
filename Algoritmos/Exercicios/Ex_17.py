velocidade_maxima = 80
multa_por_km = 5

velocidade_carro = input("Qual a velocidade do carro? ")

try:
    velocidade_carro = int(velocidade_carro)
    velocidade_ultrapassado = velocidade_carro - velocidade_maxima

    if velocidade_ultrapassado > 0:
        multa_total = velocidade_ultrapassado * multa_por_km
        print(f'Você ultrapassou a velocidade em {velocidade_ultrapassado}km/h, logo será multado em R${multa_total:.2f}')
    else:
        print("Você está dirigindo dentro da velocidade permitida")

except:
    print('O valor preenchido não é um número')