"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 03/04/2023

"""

# Ex2 - Fazer um programa em que o usuário digita o raio de um circunferência e o programa imprime na tela o seu comprimento.

# Importação da biblioteca math
import math

# Declaração da variável
print("Informe, por gentileza, o raio da circunferência: ")
raio = float(input())

# Calcular o comprimento
comprimento =  2 * math.pi * raio

# Imprimir na tela
print("O comprimento da circunferência é: ", comprimento)
