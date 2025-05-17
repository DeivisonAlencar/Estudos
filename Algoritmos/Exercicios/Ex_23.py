desc_fem = 13
desc_mas = 5

nome = input('Digite seu nome: ')
genero = input('Digite seu genero (F/M): ')
compras = input('Digite o valor de suas compras: ')

try:
    compras = float(compras)
except:
    print('O valor digitado não é um numero')

if genero == 'F':
    desconto = (compras/100) * desc_fem
elif genero == 'M':
    desconto = (compras/100) * desc_mas

print(f'Olá {nome}, o seu desconto será de R${desconto:.2f} e você pagará R${compras - desconto:.2f}')