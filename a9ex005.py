from random import randint

vet = [] #vetor vazio
pos = [] #vetor dos números positivos
semdup = [] #vetor dos números positivos sem repetição
for i in range(20):
    vet.append(randint(-10, 10)) #gera um vetor com números de -10 a 10 
    if (vet[i] > 0): #estamos considerando que 0 não é positivo
        pos.append(vet[i])
for i in range(len(pos)):
    #a função count retorna a quantidade de vezes que determinado elemento se repete em um vetor, ou seja, se retornar 0, é porque o elemento não está presente
    if semdup.count(pos[i]) == 0:
        semdup.append(pos[i])
print(f"Vetor lido: {vet}\n")
print(f"Vetor com os numeros positivos: {pos}\n")
print(f"Vetor com os numeros positivos e sem repeticao: {semdup}\n")