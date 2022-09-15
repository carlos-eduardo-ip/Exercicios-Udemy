numeros = int(input('Quantos números você vai digitar? '))

vetor = [0 for x in range (numeros)]

for i in range(numeros):
    vetor[i] = int(input('Digite um número: '))

for i in range(numeros):
    if vetor[i] < 0:
        print(vetor[i])
