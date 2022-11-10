from random import randint

vet = [] #vetor vazio
qtd = 0 #quantidade de vezes que saiu o número 6
per = 0 #percentual dos lançamentos
print("LANÇANDO O DADO...")
for i in range(50):
    n = randint(1, 6) #gera números inteiros de 1 a 6
    vet.append(n)
    if n == 6:
        qtd += 1 #é o mesmo que escrever qtd = qtd + 1
print(f"Resultado dos lancamentos: {vet}")
per = qtd*2
print(f"O numero 6 representa {per}% dos lancamentos")