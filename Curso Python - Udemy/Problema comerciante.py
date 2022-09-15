numeros = int(input('Serão digitados dados de quantos produtos? '))

nome_do_produto = []
preco_de_compra = []
preco_de_venda = []

for i in range(numeros):
    i += 1
    print(f'Produto {i}')
    nome_do_produto.append(input('Nome do produto: '))
    preco_de_compra.append(float(input('Preço de compra: ')))
    preco_de_venda.append(float(input('Preço de venda: ')))

lucro_10 = 0
lucro_10_20 = 0
lucro_20 = 0
total_de_compras = 0
total_de_vendas = 0

for i in range(numeros):
    total_de_compras += preco_de_compra[i]
    total_de_vendas += preco_de_venda[i]
    
    if (((preco_de_compra[i] - preco_de_venda[i]) * 100) / preco_de_venda[i]) <= 10:
        lucro_10 += 1
    if (((preco_de_compra[i] - preco_de_venda[i]) * 100) / preco_de_venda[i]) <= 20:
        lucro_10_20 += 1
    else:
        lucro_20 += 1

print('Relatorio: ')
print(f'Lucro abaixo de 10%: {lucro_10}')
print(f'Lucro entre 10% e 20%: {lucro_10_20}')
print(f'Lucro acima de 20%: {lucro_20}')
print(f'Valor total de compra: R$ {total_de_compras:.2f}')
print(f'Valor total de venda: R$ {total_de_vendas:.2f}')
print(f'Lucro total: R$ {total_de_vendas - total_de_compras:.2f}')