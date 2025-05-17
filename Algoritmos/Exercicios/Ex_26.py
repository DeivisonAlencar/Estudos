vet = [5,9,0,6]
n = len(vet)

troca = 0


for i in range(0,n-1):
    for j in range(i+1,n):
        if vet[i] > vet[j]:
            troca = vet[j]
            vet[j] = vet[i]
            vet[i] = troca

print(vet)           
