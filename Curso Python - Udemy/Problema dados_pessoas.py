numeros = int(input('Quantas pessoas serão digitadas? '))

altura = []
genero = []
media_altura_f = 0

numeros_m = 0
numeros_f = 0

for i in range(numeros):
    i += 1
    altura.append(float(input(f'Altura da {i}° pessoa: ')))
    genero.append(input(f'Genero da {i}° pessoa: '))
    i -= 1
    if genero[i] == 'F' or genero[i] == 'f':
        media_altura_f += altura[i]
        numeros_f += 1
    elif genero[i] == 'M' or genero[i] == 'm':
       numeros_m += 1 

maior_altura = altura[0]
menor_altura = altura[0]

for i in range(numeros):
    if altura[i] > maior_altura:
        maior_altura = altura[i]
    if altura[i] < menor_altura:
        menor_altura = altura[i]

print(f'Menor altura = {menor_altura}')
print(f'Maior altura = {maior_altura}')
print(f'Media das alturas das mulheres = {media_altura_f / numeros_f:.2f}')
print(f'Número de homens = {numeros_m}')
