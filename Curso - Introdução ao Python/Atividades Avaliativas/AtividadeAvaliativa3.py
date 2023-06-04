"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 12/04/2023

"""

## Solicita ao usuário a quantidade de unidades vendidas

meta = 50000
vendas = int(input("Digite o número de unidades vendidas: "))

## Verifica se as metas foram atingidas e exibe o resultado para o usuário

if vendas < meta:
    print("A meta não foi atingida. Ninguém recebe bônus.")
elif vendas <= meta + 500:
    bonus = vendas * 0.05
    print("A meta foi atingida com sucesso! Os vendedores receberão um bônus de 5% sobre as vendas:")
    print(f"R${bonus:.2f}")
else:
    bonus = vendas * 0.15
    print("A meta foi ultrapassada em mais de 500 unidades! Os vendedores receberão um bônus de 15% sobre as vendas:")
    print(f"R${bonus:.2f}")
