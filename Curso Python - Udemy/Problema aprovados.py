numeros = int(input('Quantos alunos serão digitados? '))

nomes = []
semestre1 = []
semestre2 = []
notas = 0

for i in range(numeros):
    i += 1
    nomes.append(input(f'Digite o nome, primeira e segunda nota do {i}° aluno: '))
    semestre1.append(float(input('Nota do primeiro semestre: ')))
    semestre2.append(float(input('Nota do segundo semestre: ')))

print('Alunos aprovados: ')

for i in range(numeros):
    if ((semestre1[i] + semestre2[i]) / 2) >= 6:
        print(nomes[i])
