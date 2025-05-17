# Conversão de tipos, coerção
# Type convertion, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutavies e primitivos:
# str, int, float, bool


print(1 + 1) # Retorna 2, uma vez que faz a soma dos numeros

print('a' + 'b') # Retorna 'ab', uma vez que concatena os textos

print(1 + 1.2) # Retorna 2.2, umma vez que soma um nº inteiro com um nº float

# Se solicitarmos o código: 
# print('1' + 1)
# Tomaremos um type erro, uma vez que ele não consegue somar uma str com um int

# Nesse caso solicitamos a conversão do tipo

print(int('1') + 1) # Retorna 2, uma vez que tranforma o '1' em inteiro antes de executar a soma

print('a' + str(1)) # Retorna 'a1', uma vez que transforma o 1 em str antes na concatenação

print(float(2)) # Retorna 20.0, uma vez que tranforma o 2 em float antes de executar

print(int(2.9)) # Retorna 2, uma vez que só extrai o valor inteiro do nº decimal

print(bool()) # Retorna False, uma vez que o bool está vazio

print(bool(' ')) # Retorna True, uma vez que há um valor preenchido, mesmo que um espaço