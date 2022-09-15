numeros = int(input('Quantas pessoas você vai digitar? '))

nome = []
idade = []
mais_velha = 0

for i in range(numeros):
    i += 1
    print(f'Dados da {i}a pessoa:')
    nome.append(input('Nome: '))
    idade.append(int(input('Idade: ')))
    
for i in range(numeros):
    if idade[i] > mais_velha:
        mais_velha = idade[i]
        pessoa = i

print(f'Pessoa mais velha: {nome[pessoa]}')
