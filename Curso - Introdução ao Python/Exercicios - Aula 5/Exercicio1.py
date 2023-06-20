"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 24/04/2023

"""
## Ex1 - Criar uma lista com todas as letras minúsculas do alfabeto.

# Cria uma lista vazia chamada "letras"
letras = []

# Utiliza um loop "for" para percorrer o intervalo de valores correspondente às letras minúsculas do alfabeto na tabela ASCII

# Os valores variam de 97 a 122, correspondentes aos códigos ASCII das letras "a" a "z"
for letra in range(97, 123):
## A cada iteração do loop, a função "chr()" é utilizada para converter o valor numérico correspondente à letra em um caractere, o caractere é adicionado à lista "letras" utilizando o método "append()"
    letras.append(chr(letra))

# Exibe a lista "letras" na tela utilizando a função "print()", que exibe todos os caracteres da lista separados por vírgula e espaço
print(letras)
