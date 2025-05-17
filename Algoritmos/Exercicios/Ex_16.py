temp_perd_por_cigarro = 10
qtd_cigarros_perd_dia = 1440/temp_perd_por_cigarro


qtd_cigarros_dia = input("Quantos cigarros você fuma por dia ? ")
anos_fumando = input("Quantos anos você é fumante? ")

try:
    qtd_cigarros_dia = int(qtd_cigarros_dia)
    anos_fumando = int(anos_fumando)

    cigarros_fumados = (anos_fumando*365) * qtd_cigarros_dia 
    dias_perdidos = cigarros_fumados / qtd_cigarros_perd_dia

    print(f'Fumando {qtd_cigarros_dia} por dia a {anos_fumando} anos, já foi perdido {dias_perdidos:.0f} dias de vida!')
except:
    print('Um dos valores apresentados não é um número')