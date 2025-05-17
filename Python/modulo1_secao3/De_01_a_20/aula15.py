# A função input, serve ppara extrair uma informação do usuario em formato de str
nome = input('Qual o seu nome? ')
print(f'Seu nome é {nome}')

# Se eu pedisse para que o usuário digitasse dois números e pedisse a soma desses numeros, oq ocorreria seria a concatenação
# O modo correto é tranformar o texto em números antes de solicitar a soma

numero_1 = input('digite um número ')
numero_2 = input('digite mais um número ')
soma = int(numero_1) + int(numero_2)
print(f' a soma de {numero_1} e {numero_2} é igual a {soma}')