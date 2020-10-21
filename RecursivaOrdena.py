l = [5, 8, 11, 3, 1, 99, 49, 57, 6, 98]
i = 2
maior = 0
if l[0] > l[1]:
    maior = l[0]
else:
    maior = l[1]

def ordena(lista):
    global i
    global maior
    while i < len(lista):
        if maior < lista[i]:
            maior = lista[i]
        i = i + 1
        ordena(lista)

ordena(l)

print("O maior numero e:", maior)
