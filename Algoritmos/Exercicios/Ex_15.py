val_hr_trab = 25
hr_trab_dia = 8

val_dia = val_hr_trab * hr_trab_dia

dias_trab = input('Quantos dias você trabalhou esse mês? ')

try:
    dias_trab = int(dias_trab)
    salario_mes = val_dia * dias_trab
    
    print(f'Com {dias_trab} dias trabalhados, e um valor diario de R${val_dia:.2f}, o seu salario do mês será R${salario_mes:.2f}')
except:
    print("O valor digitado não é um número")