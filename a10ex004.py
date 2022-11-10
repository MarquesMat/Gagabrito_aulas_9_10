#se quiser listas com características aleatórios, veja o gabarito do ex3
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista_intercalada = []

#a menor lista será chamada de l1 e, a maior, de l2
if len(lista1) < len(lista2):
    menor = len(lista1)
    l1 = lista1
    l2 = lista2
else:
    menor = len(lista2)
    l1 = lista2
    l2 = lista1
i = 0

#começar pela menor lista
while(i<menor):
    lista_intercalada.append(l1[i])
    lista_intercalada.append(l2[i])
    i += 1

#completar com os itens que restaram da maior lista
while(i<len(l2)):
    lista_intercalada.append(l2[i])
    i += 1
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista intercalada: {lista_intercalada}")