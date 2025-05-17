# Os id são os locais onde as memorias são guardadas, no caso a baixo:
# As variaveis nome e nome2 possuem o mesmo id por terem o mesmo valor
# mas a variavel nome3 já possui um id diferente

nome = 'a'
nome2 = 'a'
nome3 = 'b'

print(id(nome))
print(id(nome2))
print(id(nome3))
