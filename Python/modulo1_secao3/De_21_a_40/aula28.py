# Fatiamento de string
# [i:f:p]
# i = inicio 
# f = fim
# p = parcial/pula

nome = 'Deivison santos de alencar'

print(nome[9:20]) # Retorna do 10º ao 20º caracter
print(nome[9:]) # Retorna do 10º caracter até o fim da string.
 
print(nome[:12]) # Retorna do inicio da string ao 12º caracter
print(nome[7:15]) # Retorna do 8º ao 15º caracter

# é possivel ainda pular caracter

print(nome[::2]) # Para cada caracter retornado, pula-se outro

# É possivel também retornar a string de traz pra frente

print(nome[::-1]) # Nesse caso a string é retornada de tras pra frente

# A função len é utilizada para verificar a quantidade de caracteres em uam strig

print(len(nome))

print(nome[10:len(nome)-1]) 
# Nesse caso estamos retornado do 10º caracter até o penultimo caracter de forma dinamica,
# Uma vez que estamos utilizando a função len para identificar quantos caracteres tem a string, e retirando uma
