dis_curt = 200
pre_curt = 0.50
pre_long = 0.45

distancia = input('Digite a distancia que voê deseja percorrer em km: ')

try:
    distancia = int(distancia)
except:
    print('O valor preenchido não é um numero')

if distancia <= dis_curt:
    preco = distancia * pre_curt
else:
    preco = distancia * pre_long

print(f'Você pagará R${preco:.2f} em sua viagem de {distancia}km')