numeros = int(input('Quantos elementos vai ter o vetor? '))

vetor = []
soma = 0
pares = 0

for i in range(numeros):
    
    vetor.append(int(input('Ditite um número: ')))
    if (vetor[i] % 2) == 0:
        soma += vetor[i]
        pares += 1

if pares > 0:
    print(f'Media dos pares = {(soma / pares)}')
else:
    print('Nenhum número par!')
