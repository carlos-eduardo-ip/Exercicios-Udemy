numeros = int(input('Quantos números você vai digitar? '))
soma = 0

vetor = [0 for x in range(numeros)]

for i in range(numeros):
    vetor[i] = float(input('Digite um número: '))

print(vetor)

for i in range(0, numeros):
    soma += vetor[i]

print(soma)
soma = 0

for i in range(0, numeros):
    soma += vetor[i]

soma = soma / numeros

print(soma)
