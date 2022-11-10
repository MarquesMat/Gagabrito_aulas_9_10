#Insertion Sort
vet = [2, 5, 3, 7, 6, 1, 9, 8, 10, 4] #vetor de exemplo
comp = 0 #número de comparações
print(f"Vetor original: {vet}")
print("\nOrdenando vetor...\n")
for i in range(1, len(vet)):
    n = vet[i]
    j = i - 1
    while j>= 0 and vet[j] > n:
        vet[j+1] = vet[j]
        j -= 1 #é o mesmo que j = j - 1
        comp += 1
    vet[j+1] = n
print(f"Vetor ordenado: {vet}")
print(f"Foram realizadas {comp} comparacoes")