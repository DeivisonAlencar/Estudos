# # Numeros inteiros e float

print(1, 2, -1, 0, sep='\r\n')
# Todos os numeros sem 'decimais' são números do tipo int -> inteiro
# Sejam eles, positivos, negativos, ou zero
# Quando o numero não tem sinal, ele automaticamente é positivo

print('\r\n') # só pulando linha

print(1.1, 2.5, -1.6, 0.0, sep='\r\n')
# Já os numeros decimais são separados por '.' e são do tipo float
# também podem ser positivos, negativos, ou zero
# Da mesma forma que os inteiros, quando não há sinal, eles automaticamente são positivos

print('\r\n') # só pulando linha

# A função (que na verdade é clasdificada como uma classe) 'type' mostra o a tipagem inferida pelo python aquele dado:
print(type('Deivison'))
print(type("Deivison"))
print(type(1.1), type(-2.5), type(0.0), sep='\r\n')
print(type(1), type(-5), type(0), sep='\r\n')
