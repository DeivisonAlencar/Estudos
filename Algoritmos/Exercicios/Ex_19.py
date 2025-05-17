nome = input('Digite seu nome: ')
nota_1 = input('Digite a primeira nota: ')
nota_2 = input('Digite a segunda nota: ')

try:
    nota_1 = float(nota_1)
    nota_2 = float(nota_2)
    media = (nota_1+nota_2)/2

    if media < 7:
        aproveitamento = 'não teve'
    else:
        aproveitamento = 'teve'

    print(f'A média do aluno {nome} é {media}, logo o mesmo {aproveitamento} bom aproveitamento')
except:
    print('Uma das notas digitas não é um numero')