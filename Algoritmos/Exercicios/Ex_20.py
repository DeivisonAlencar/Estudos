numero = input('Digte um numero inteiro ')

try:
    numero = int(numero)
    resto = numero % 2

    if resto == 0:
        print('O valor digitado é par')
    else:
        print('O valor digitado é impar')
except:
    print('O valor digitado não é um numero inteiro')