alistamento = 18

idade = input('Digite a sua idade: ')

try:
    idade = int(idade)
    
    if idade < alistamento:
        print(f'Você ainda não pode se alistar, faltam {alistamento - idade} anos')
    elif idade == alistamento:
        print('Você está na idade exata para se alistar')
    else:
        print(f'Você já está alistado a {idade - alistamento} anos')
except:
    print('O valor digitado não é um número')