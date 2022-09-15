numeros = int(input('Quantos números você vai digitar? '))

vetor = []
maior_posicao = 0

for i in range(numeros):
    vetor.append(float(input('Digite um número: ')))

for i in range(numeros):
    if vetor[i] > maior_posicao:
        maior_posicao = vetor[i]
        posicao = i

print(f'Maior valor = {maior_posicao:.1f}')
print(f'Posição do maior valor = {posicao}')
