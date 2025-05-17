nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:

    nome_invertido = nome[::-1]
    quant_letras = len(nome)
    pri_letra = nome[0]
    ult_letra = nome[quant_letras-1]
    espacos = ' ' in nome

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    
    if espacos == True:
        print('Seu nome possui espacos')
    else:
        print('Seu nome não possui espaços')
    
    print(f'Seu nome possui {quant_letras} caracteres')
    print(f'A primeira letra do seu nome é "{pri_letra}"')
    print(f'A ultima letra do seu nome é "{ult_letra}"')
else:
    print('Desculpe, você deixou campos vazios')