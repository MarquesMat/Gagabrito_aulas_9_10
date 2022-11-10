#Bubble Sort
vet = [2, 5, 3, 7, 6, 1, 9, 8, 10, 4] #vetor de exemplo
comp = 0 #número de comparações
print(f"Vetor original: {vet}")
print("\nOrdenando vetor...\n")
for i in range(len(vet)):
    for j in range(len(vet)-i-1):
        comp += 1
        if vet[j] > vet[j+1]:
            temp = vet[j]
            vet[j] = vet[j+1]
            vet[j+1] = temp
print(f"Vetor ordenado: {vet}")
print(f"Foram realizadas {comp} comparacoes")