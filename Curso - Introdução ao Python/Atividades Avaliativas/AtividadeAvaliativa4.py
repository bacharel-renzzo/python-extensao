"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 19/04/2023

"""

## Quantidade de itens vendidos por cada vendedor de uma loja/O quanto de bônus que ele irá receber

vendas = [100, 150, 1500, 2000, 120]
salarios = [1000, 1500, 2000, 2500, 1200]
bonus = []

## Calculo de bônus +  salário

for i in range(len(vendas)):
 if vendas[i] > 1000:
  bonus.append("Vendedor " + str(i+1))
salarios[i] *= 1.15

## Exibe ao usuário os vendedores que conseguiram os bônus

print("Os vendedores que conseguiram o bônus foram: ")
for v in bonus:
  print(v)
