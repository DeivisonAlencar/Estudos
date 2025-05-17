nome = 'Deivison'
altura = 1.72
peso = 80
imc = peso / (altura ** 2) 

# precisar preencher vairas informações entre aspas sempre que se referir a uma variavel pode ser ajustado usando o f-strig
# print(nome, 'tem', altura, 'de altura, ele pesa', peso, 'kg e seu imc é de', imc)

# basta incluir um f antes da nossa string e colocar nossas variaveis entre chaves
linha1 = f'{nome} tem {altura} de altura,'
linha2 = f'pesa {peso} e seu imc é de' 
linha3 = f'{imc:.2f}'
# Com o f-tring podemos inclusive determinar a quantidade casas decimais de um nº float como acima
# basta incluir a quantidade de casas decimais que se quer entre a varivel, dois pontos, ponto e f

print(linha1, linha2, linha3, sep='\r\n')
