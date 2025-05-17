condicao1 = False
condicao2 = True
condicao3 = False
condicao4 = True

if condicao1:
    print('Condição 1 é verdadeira')
elif condicao2:
    print('Condição 2 é verdadeira')
elif condicao3:
    print('Condição 3 é verdadeira')
elif condicao4:
    print('Condiçao 4 é verdadeira')
else:
    print('Nenhuma das condições são verdadeiras')

print('Suas condições foram validadas')

# As validações são feitas de cima pra baixo, e sempre que uma condição for verdadeira, as demais validações não são realizadas
# Ponto importante que podemos depurar o código linha por linha através do debugador