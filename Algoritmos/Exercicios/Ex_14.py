dias_alugados = input('Quantos dias o carro foi alugado? ')
km_rodados = input('Quantos km foram percorridos? ')

valor_diaria = 90
valor_km_percorrido = 0.20

try:
    dias_alugados = int(dias_alugados)
    km_rodados = float(km_rodados)
    
    total_diarias = dias_alugados * valor_diaria
    total_percurso = valor_km_percorrido * km_rodados

    total_a_pagar = total_diarias + total_percurso

    print(f'Após {dias_alugados} dias com o carro e com um total de {km_rodados}km rodados o valor total a ser pago é de R${total_a_pagar:.2f}. R${total_diarias:.2f} das diarias e R${total_percurso:.2f} pelo percurso')

except:
    print('Um dos valores preenchidos não são numeros')