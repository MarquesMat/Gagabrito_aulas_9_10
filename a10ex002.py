from random import randint

vet = []
qtd = []
for i in range(10):
    vet.append(randint(1,6))
for i in range(1, 7): #i varia de 1 a 6
    qtd.append(vet.count(i))
print(vet)
print(qtd)