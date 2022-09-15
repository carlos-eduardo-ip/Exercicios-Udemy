numeros = int(input('Quantas pessoas serão digitadas? '))

nome = []
idade = []
altura = []

for i in range(numeros):
    i +=  1
    print(f'Dados da {i}° pessoa: ')
    nome.append(str(input('Nome: ')))
    idade.append(int(input('Idade: ')))
    altura.append(float(input('Altura: ')))

soma_altura = 0
for i in range(numeros):
    soma_altura += altura[i]

altura_media = soma_altura / numeros

porcentagem_idade = 0
for i in range(numeros):
    if idade[i] < 16:
        porcentagem_idade += 1

menor = (float(porcentagem_idade) / numeros) * 100.0

print(f'\nAltura média: {altura_media}')
print(f'Pessoas com menos de 16 anos: {menor:.1f}%')

for i in range(numeros):
    if idade[i] < 16:
	    print(nome[i])
