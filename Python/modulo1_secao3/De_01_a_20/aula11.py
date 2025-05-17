# Precedencia de operadores
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_errada = 1 + 1 ** 5 + 5 
print(conta_errada)

conta_correta = (1 + 1) ** (5 + 5)
print(conta_correta)