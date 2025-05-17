numero_str = input('Digite um nº inteiro: ')

try:
    numero_int = int(numero_str)
    resto = (numero_int % 2)
    if not resto:
        print('Seu numero é par')
    else:
        print('Seu numero é impar')
except:
    print('Você não digitou um numero inteiro')

print(10 * '-')

horario = input('Que horas são? ')

MANHA_I = 0
MANHA_F = 11
TARDE_I = 12
TARDE_F = 17
NOITE_I = 18
NOITE_F = 23

try:
    hora = horario[0:2]
    hora_int = int(hora)
    p_manha = hora_int >= MANHA_I and hora_int <= MANHA_F
    p_tarde = hora_int >= TARDE_I and hora_int <=TARDE_F
    p_noite = hora_int >= NOITE_I and hora_int <= NOITE_F

    if p_manha:
        print('Bom dia')
    elif p_tarde:
        print('Boa tarde')
    elif p_noite:
        print('Boa noite')
except:
    print('Você não digitou uma hora valida')

print(10 * '-')

nome = input('Digite seu nome: ')
tam_nome = len(nome)

N_CURTO = 4
N_LONGO = 6

nome_curto = tam_nome <= N_CURTO
nome_normal = tam_nome > N_CURTO and tam_nome < N_LONGO
nome_longo = tam_nome > N_LONGO

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
elif nome_longo:
    print('Seu nome é longo')