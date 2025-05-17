""" 
interpolação de strings
s - string
d ou i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Deivison'
preco = 100.9875
texto = 'Olá %s o preço é de %.2f' %(nome, preco)

print(texto)

# Nesse caso utilizamos o simbolo de % junto a letra do tipo de informação para recuperar o valor de uma variavel
# E adicionamos as variaveis tbm entre parenteses depois de um % no fim da string

print(10 * '-')

numero = 200
texto2 = 'O exadecimal de %i é %x' %(numero, numero)

print(texto2)

# Para cada valor inteiro, é atribuido um exadecimal
# Podemos recuperar ele com quatro casas = %04x ou com oito casas = %08x
# Além disso podemos também recupera-los de forma minuscula = %x ou maiscula = %X