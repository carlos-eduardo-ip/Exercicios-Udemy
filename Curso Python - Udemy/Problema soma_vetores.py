numeros = int(input('Quantos valores vai ter cada vetor? '))

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(numeros):
    vetor_a.append(int(input('Digite os valores do vetor A: ')))

for i in range(numeros):
    vetor_b.append(int(input('Digite os valores do vetor B: ')))

for i in range(numeros):
    vetor_c.append(int(vetor_a[i] + vetor_b[i]))

print('Vetor resultante: '), print('\n'.join(map(str, vetor_c)))
