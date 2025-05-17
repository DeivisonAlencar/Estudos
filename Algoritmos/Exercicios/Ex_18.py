idade_votacao_opcional_1 = 16
idade_votacao_obrigatorio = 18
idade_votacao_opcional_2 = 65

idade = input('Digite a sua idade: ')

try:
    idade = int(idade)

    if idade < idade_votacao_opcional_1:
        print('Você ainda não possui idade para votar')
    elif idade < idade_votacao_obrigatorio:
        print('Você tem a opção de votar')
    elif idade < idade_votacao_opcional_2:
        print('Você possui a obrigação de votar')
    else:
        print('Você tem a opção de votar')
except:
    print('O valor preenchido não é um número')