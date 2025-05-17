"""
OP      Significado         exemplo
>       maior               2 > 1
>=      maior ou igual      2 >= 2
>       menor               1 < 2
<=      menor ou igual      1 <= 1           
==      igual               'a2' == 'a2'
!=      diferente           'B' != 'b'
"""

maior = 2 > 1

maior_igual = 2 == 2

menor = 1 < 2

menor_igual = 1 <= 1

igual = 'a2' == 'a2'

diferente = 'B' != 'b'

teste = 'Deivison'
# Para usar no terminal:
# Podemos realizar teste interativos no proprio terminal da seguinte maneira:
# python -i aula19.py Para definir qual projeto queremos trabalhar
# Depois disso basta digitar a variavel que queremos validar, que será mostrado o resultado
# Quando eu quiser encerrar a conexão basta digitar: quit()

# importante, caso eu altere alguma coisa no arquivo, preciso encerrar a conexão e criar ela dnv
# no caso do codigo abaixo, eu só consigo validar o resultado da varivel depois de excuta-la

if 1 == 1:
    conexao = 'conexão1'
else:
    conexao = 'conexão2'