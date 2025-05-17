""" A função  'print' serve para exibir
um determinado texto em tela """

print(12, 34) 

""" A virgula serve de separador de componente
nos casos de print a separação padrão entre os textos é um espaço
mas podemos alterar através do parametro 'sep' """

print(12, 34, sep='-')

""" Também por padrão há um 'finalizador' 
que pula para a próxima linha no fim de cada código
esse finalizador se dá de forma oculta: CRLF = \r\n
mas podemos alterar através do parametro 'end' """

print(10, 11, sep='-', end='.\r\n')
print(12, 13)

# Nesse caso ele não pula linha de um código para o outro, pois o 'finalizado' do código agora é o '.'
# O python faz diferença entre letras maiusculas e minusculas, então cuidado