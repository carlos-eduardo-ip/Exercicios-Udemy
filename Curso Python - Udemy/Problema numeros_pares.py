numeros = int(input('Quantos números você vai digitar? '))

vetor = []
pares = []

for i in range(0, numeros):
    vetor.append(int(input('Digite um número: ')))

    if (vetor[i] % 2) == 0:
        pares.append(vetor[i])

print('Números pares: '), print(' '.join(map(str, pares)))
print('Quantidade de pares = ', len(pares))
