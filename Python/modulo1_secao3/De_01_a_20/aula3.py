"""
Python = linguagem de programação com
tipo de tipagem = Dinamica / forte
"""
# Tipo de dados str -> string -> texto
# Pode ser escrito entre aspas simples ou aspas duplas

print('Deivison')
print("Deivison")
# Não há diferença de execução dos códigos acima

# Caso você queira exibir um texto que contenha aspas, há dois jeitos:
# Se usassemos: print("Deivison "Santos de Alencar") 
# o sistema entenderia que estou fechando as aspas logo depois do espaço e traria erro 

# Escape:
print("Deivison \"Santos de Alencar")
print("Deivison \"Santos\" de Alencar")
# Ao utilizar a '\' o próximo caracter é ignorado, sendo assim ele não entende essa aspas como 'fechamento'

#r:
#Caso você queira também exibir o caracter de escape, podemos utilizar o r no inicio do cógido:
print(r"Deivison \"Santos\" de Alencar")

# Porem o jeito mais fácil é utilizar a composição de aspas simples e aspas duplas:

# Se o meu texto precisa conter uma aspas simples, eu o coloco entre aspas duplas:
print("Deivison 'Santos' de Alencar")

# Se o meu texto precisa conter uma aspas duplas, eu o coloco entre aspas simples:
print('Deivison "Santos" de Alencar')