salario_atual = input('Digite o seu salario atual ')

try:
    salario_atual = float(salario_atual)
    aumento = (salario_atual /100) * 15
    novo_salario = salario_atual + aumento

    print(f'Após um aumento de 15% o salario passou de R${salario_atual:.2f} para {novo_salario:.2f}')
except:
    print('O valor digitado não é um número')