vet = [] #vetor vazio
res = -1 #resposta
print("PREENCHA O VETOR:")
for i in range(1, 6): #a letra i vai variar de 1 a 5
    n = int(input(f"VALOR {i}: "))
    vet.append(n)
x = int(input(f"\nDIGITE O VALOR PROCURADO: "))
for i in range(len(vet)): #len(vet) == 5
#esse programa irá comparar cada item de vet a x, quando for igual, res irá mudar de valor
#obs: qualquer posição que res receber será >= 0, logo esse if não será cumprido após a primeira ocorrência
    if (vet[i] == x) and (res < 0):
        res = i
if(res >= 0):
    print(f"\nO valor {x} esta na posicao {res}")
else:
    print(f"\nO valor {x} nao foi encontrado")