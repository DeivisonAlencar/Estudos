continuar = True

def par(n):
    if n%2 == 0:
        return n
    else:
        return n+1

while continuar:
    x = int(input('Digite um número qualquer: '))

    if x < 0:
        print('Trabalhamos melhor com numeros positivos, que tal tentar um outro numero ?')
    elif x == 0:
        print('OK, acabamos por aqui!')
        continuar = False
    else:
        n_par = par(x)
        soma = n_par
        for i  in range(0,4):
            n_par += 2
            soma += n_par 
        
        print(soma)