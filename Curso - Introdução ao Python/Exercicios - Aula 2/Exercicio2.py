"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 10/04/2023

"""

# Ex2 - Calculadora de preço da laranja - Cada laranja custa R$0.3, mas quando comprada acima de uma dúzia, seu valor cai para R$0.25 cada

# Declarar a entrada da quantidade de laranjas a ser comprada
print("Informe, por gentileza, a quantidade de laranjas a serem compradas: ")
quantidade_de_laranjas = int(input())

# Declaração do if
if(quantidade_de_laranjas > 12):
    preco_das_laranjas = quantidade_de_laranjas * 0.25

# Declaração do else
else:
    preco_das_laranjas = quantidade_de_laranjas * 0.3

# Imprimir na tela a mensagem: "x laranjas por Y reais totaliza: R$ Z"
print("O preço das laranjas é:", preco_das_laranjas)
    
