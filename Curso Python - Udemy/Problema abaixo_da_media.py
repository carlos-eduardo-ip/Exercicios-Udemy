numeros = int(input('Quantos elementos vai ter o vetor? '))

vetor = []
abaixo_da_media = []
media_vetor = 0

for i in range(numeros):
    vetor.append(float(input('Digite um número: ')))
    media_vetor += vetor[i]

media_vetor = media_vetor / numeros

print(f'Media do vetor = {media_vetor:.3f}')
print('Elementos abaixo da media')
for i in range(numeros):
    if vetor[i] < media_vetor:
        abaixo_da_media.append(float(vetor[i]))
       
print('\n'.join(map(str, abaixo_da_media))) 
