# Outras formatações com f-strings
# podemos utilizar os sinais <>^ para definir a quantidade de caracteres de uma string

cpf = 6838362503
cpf_completo = (f'{cpf:0>11}')
print(cpf_completo)
# Aqui definimos que um CPF deve ter no 11 digitos, e que caso não possua, deve ser completado com 0 a esquerda

print(10 * '-')

texto = 'ABC'
texto_completo = (f'O texto completo é {texto:-<10}')
print(texto_completo)
# Aqui definimos que o texto deve ter 10 digitos, e caso não possua, deve ser completado com - a direita

print(10 * '-')

meio = 'AAAA'
completo = (f'{meio:k^8}')
print(completo)
# Aqui definimos que o nome deve ter 8 digitos, e caso não possua, deve ser completado com k entre direira e esquerda