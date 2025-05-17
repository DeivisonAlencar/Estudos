# No python, quando falamos de boleanos,  siginifca false e  significa verdadeiro

if 0 and 1:
    print('true1') 
    # Nesse caso essa linha não será exacutada, pois 0 define o if como False, mesmo que tenhamos o 1 como True

if 1 and 1:
    print(True and 0 and 1) 
    # Nesse caso essa linha será executada e retornará 0, pois apesar de  termos o 'True' e o 1, a condição 0 faz como que todo o textp assuma false

if 1 and True:
    print(1 and True)
    print(True and 1)
    # Nesse caso as duas linhas serão executadas, e cada uma retornará o ultimo argumento, a primeira linha retornará 'True' e a segunda 1

acao = input('Digite "E" para entrar e "S" para sair ')
senha = input('Digite a sua senha ')
senha_verificacao = '123456'

if acao == 'E' and senha == senha_verificacao:
    print('Você está entrando')
elif acao == 'S':
    print('Vocês está saindo')
else:
    print('Sua senha está incorreta, ou você digitou um comando não existente')