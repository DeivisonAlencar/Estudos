# try e except

# No dia a dia dos nossos códigos podemos ter alguns erros, ou as chamadas excessões no python

numero = input('Digite um numero para ser duplicado: ')
numero_duplicado = (numero * 2)
print(numero_duplicado) 
# Retorna erroneamente 22, uma vez que um input sempre retorna uma string
# fazendo-se necessário transformar o valor informado pelo usario em nº antes de realizar a multiplicação

print(10 * '-')

numero2 = input('Digite um 2º numero para ser duplicado: ')
numero2_int = int(numero2)
numero2_duplicado = (numero2_int * 2)
print(numero2_duplicado)
# Dessa maneira, o cógido funciona, desde que o usuario informe apenas nº, caso informe outro tipo, teremos um erro

print(10 * '-')

# Esse erro pode ser contornado de algumas maneiras, com o if:
numero3 = input('Digite um 3º numero para ser duplicado: ')
if numero3.isdigit():
    numero3_int = int(numero3)
    numero3_duplicado = (numero3_int * 2)
    print(numero3_duplicado)
else:
    print('Você precisa digitar um numero')

print(10 * '-')

# Ou com o try an except:

numero4 = input('Digite um 4º numero para ser duplicado: ')
try:
    numero4_int = int(numero4)
    numero4_duplicado = (numero4_int * 2)
    print(numero4_duplicado)
except:
    print('Voçê não digitou um numero')