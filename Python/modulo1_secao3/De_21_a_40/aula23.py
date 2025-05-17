# O not é utilizado para inveter expressões
# Ou seja o False vira True e o True vira False

print(not False) # Retorna True
print(not True) # Retorna False
print(not 0) # Retorna True, pois o 0 é considerado False
print(not 1) # Retorna False, pois o 1 é consuderado True


senha = input('Digite sua senha: ')

if not senha:
    print('Senha não preenchida')
    # Se a senha não for digitada, a variavel receberá 'False', 
    # E incluindo o operador not na frente, transformamos em verdadeiro, logo esse código será executado
else:
    print(f'Senha {senha} cadastrada com sucesso')
    # Porem se alguma senha for preenchida, a variavek senha receberá 'True'
    # E incluindo o operadfor not na frente, tranformamos em falso, logo o código if não será executado, executando automaticamente o else