preco_total = input('Digite o preço total do produto ')

try:
    preco_total = float(preco_total)
    desconto = (preco_total / 100) * 5
    preco_com_desconto = preco_total - desconto

    print(f'Após o desconto de 5% o produto passou de R${preco_total:.2f} para R${preco_com_desconto:.2f}')
except:
    print('O valor digitado não é um número')