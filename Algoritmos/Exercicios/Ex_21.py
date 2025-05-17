ano = input('Digite um ano: ')

try:
    ano = int(ano)
    resto_div = ano % 4

    if resto_div == 0:
        print('O ano digitado é bisexto')
    else:
        print('O ano digitado não é bisexto')
except:
    print('O valor digitado não é um numero inteiro')