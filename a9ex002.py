vet = [] #vetor vazio
vet_aux = [] #vetor vazio que guardará os valores diferentes
print("PREENCHA O VETOR: ")
for i in range(1, 11):
    n = int(input(f"VALOR {i}: ")) #a letra i vai variar de 1 a 10
    vet.append(n)
#o vetor está completo
for i in range(10):
    #a função count retorna a quantidade de vezes que determinado elemento se repete em um vetor, ou seja, se retornar 0, é porque o elemento não está presente
    if  vet_aux.count(vet[i]) == 0:
        vet_aux.append(vet[i])
#agora temos um vetor auxiliar contendo apenas os números diferentes de vet
print(f"VETOR: {vet}")
print(f"Ha {len(vet_aux)} numeros diferentes no vetor.")