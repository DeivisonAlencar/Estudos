acao = input('Informe "E" para entrar ou "S" para sair ')
senha = input('Digite sua senha ')
senha_verificacao = '123456'

if (acao == 'E' or acao == 'e') and senha == senha_verificacao:
    print('Você está entrando')
# Aqui está uma validação do 'or', onde o usuario pode utilizar tanto o "E" quanto o "e"
# Ele está entre parenteses para que seja validado antes da validação da senha, caso deixe tudo na mesma linhas pode trazer ambiguidade pra validação
    
# a comparação or, considera toda uma setençã como verdadeira caso encontre algum valor verdadeiro,
# além disso ela sempre preencherá o primeiro valor verdadeiro que encontrar:
    
nova_senha = input('Escolha uma nova senha: ') or 'Senha não digitada'
print(nova_senha)
# Nesse exemplo, caso o usuario não preencha nenhuma senha, a variavel 'nova senha' vai receber o valor 'senha não digitada' uma vez que entende o 0 como valor falso, e qq outro texto como verdadeiro
