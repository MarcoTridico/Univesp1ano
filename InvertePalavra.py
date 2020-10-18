nome = input("Digite o nome ou palavra a ser invertido: ")
nomeInvertido = []
comprimento = len(nome)
i = 0
j = comprimento - 1

while i < comprimento:
    nomeInvertido.append(nome[j])
    i = i + 1
    j = j - 1

print(*nomeInvertido)