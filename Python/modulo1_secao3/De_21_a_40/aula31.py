# No python não existe explicitamente uma diferença entre variaveis e cosntantes
# Sendo assim é convenção que as variaveis que não serão auteradas, ou seja são constantes, sejam definidas em maiusculo

velocidade = 61
local = 100

RADAR_1 = 60
LOCAL_1 = 100
RANGE_1 = 1

# Jeito 1 de analise:

if velocidade > RADAR_1 and (local == LOCAL_1 or local == LOCAL_1 -1 or local == LOCAL_1 +1):
    print('Você ultrapassou a velocidade')
else:
    print('siga reto')

print(10 * '-')

# Jeito 2 de analise:
    
if local >= (LOCAL_1 - RANGE_1) and local <= (LOCAL_1 + RANGE_1) and velocidade > RADAR_1:
    print('Você ultrapassou a velocidade')
else:
    print('siga reto')

print(10 * '-')

# Jeito 3 de analise (e mais correto):

carro_no_radar = local >= (LOCAL_1 - RANGE_1) and local <= (LOCAL_1 + RANGE_1)
carro_na_velocidade = velocidade > RADAR_1

if carro_no_radar and carro_na_velocidade:
    print('Você ultrapassou a valocidade')
else:
    print('siga reto')

