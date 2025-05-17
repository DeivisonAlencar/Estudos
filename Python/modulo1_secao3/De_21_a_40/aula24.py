# Em python as  strings são iteraveis, ou seja, é possivel identificar letra a letra

#  D  E  I  V  I  S  O  N
#  0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1

# Elas podem ser  encontradas iniciando do 0, ou de trás pra frente com numeros negativos
nome = 'Deivison'
print(nome[2]) # Só é possivel buscar um indice por vez

print(10 * '-')
# in e not in são condições usadas para validar se um determinado texto está contido em outro texto

print('i' in nome) # Retornará True, pois a letra 'i' está contida no nome
print('a' in nome) # Retornará False, pois a letra 'a' não está contida no nome

print(10 * '-')

print('i' not in nome) # Retornará False, pois a letra 'i' está sim contida no nome
print('a' not in nome) # Retornará True, pois de fato a letra 'a' não est´s contida no nome

print(10 * '-')

nome = input('Digite seu nome: ')
busca = input('Digite oq você deseja buscar: ')

if busca in nome:
    print('{} está contido em {}'.format(busca, nome))
elif busca not in nome:
    print('{} não está contido em {}'.format(busca, nome))