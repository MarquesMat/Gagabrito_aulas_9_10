vet1 = [-1, 0, 2]
vet2 = [5, 8, -4]
vet3 = [] #força resultante
for i in range(len(vet1)): #len(vet1) == len(vet2) == 3
    r = vet1[i] + vet2[i] #a letra i vai variar de 0 a 2
    vet3.append(r)
print(f'A forca resutante eh {vet3}')