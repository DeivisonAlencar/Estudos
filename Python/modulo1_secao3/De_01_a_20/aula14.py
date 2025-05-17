a = 'AAAA'
b = 'BBBB'
c = 1.1

# outra forma de utilizar variaveis em strings é utilizando o metodo format
# onde incluimos chaves no meio do texto, e as variaveis logo após no 'format'
formato1 = 'a={} b={} c={}'.format(a, b, c)
print(formato1)

# Podemos tambem estabeler a string de forma separada:
string2 = 'a={} b={} c={}'
formato2 = string2.format(a, b, c)
print(formato2)
# Nesse caso temos o mesmo resultando, porém separando cada informação
# Caso eu incluisse d={} sem que houvesse uma outra variavel no meu format, tomaria um erro de fora de range (out of range)


# Por padrão, a primeira varivel do metodo format recebe o indice 0, e os demais recebem os números subsquentes
# Ou seja se meu codigo for string = 'b={}, c={} a={}' meu resultado seria b=AAAA c=BBBB a=1.1
# O jeito correto de ajustar essa ordem não é mexendo nas variaveis do format, mas sim incluindo o indice correto nas chaves
# podendo inclusive repetir algum dado novamente
string3 = 'b={1} c={2} a={0} a={0}'
formato3 = string3.format(a, b, c)
print(formato3)

#Podemos também denir nomes para nossos argumentos, criando os chamados parametros nomeados, assim não dependeno dos indices
string4 = 'a={} c={nome3} b={}'
formato4 = string4.format(a, b, nome3=c)
print(formato4)
# Dois pontos importantes: 
# 1 - quando eu defino 1 nome para um argumento, todos os subsquentes pecisam ser nomeados também
# Ou seja, posso definir apenas o nome do argumento c, mas se definir o do arqumento a, precisarei definir de todos os demais
# 2 - Depois de definido um nome, não poderei mais utilizar o incide para me referir aquele argumento

# Podemos formatar o nº da mesma maneria que formatamos antes, porém agora diretamente na string
string5 = 'a={} b={} c={:.2f}'
formato5 = string5.format(a, b, c)
print(formato5)
