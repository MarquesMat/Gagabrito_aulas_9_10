#Selection Sort
vet = [2, 5, 3, 7, 6, 1, 9, 8, 10, 4] #vetor de exemplo
comp = 0 #número de comparações
print(f"Vetor original: {vet}")
print("\nOrdenando vetor...\n")
for i in range(len(vet)):
    min = i
    for j in range(i+1, len(vet)):
        comp += 1
        if vet[j] < vet[min]:
            min = j
    (vet[i], vet[min]) = (vet[min], vet[i])
print(f"Vetor ordenado: {vet}")
print(f"Foram realizadas {comp} comparacoes")