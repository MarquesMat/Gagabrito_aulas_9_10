from random import randint

vet = []
media = 0

#essa parte do código está gerando um vetor de tamanho de 4 a 10 com números de 0 a 10
#se preferir, substitua para um vetor conhecido, ex: vet =  [2.5, 7.5, 10.0, 4.0]
#se fizer isso, não se esqueça de calcular a média
tam = randint(4, 10)
for i in range(tam):
    vet.append(randint(0, 10))
    media += vet[i]
media /= tam #é o mesmo que media = media / tam

prox = vet[0]
dif = abs(media-prox) #retorna o módulo dessa subtração
for i in range(1, tam):
    if dif > abs(media-vet[i]):
        dif = abs(media-vet[i])
        prox = vet[i]
print(f"Vetor: {vet}")
print(f"Media: {media:.1f}") #formata para 1 casa decimal
print(f"Valor mais proximo da media: {prox}")
