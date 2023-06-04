# Ex1 - Faça um programa que peça verifica se o usuário digitou um número inteiro.
# Caso tenha digitado, mostrar o número na tela.
# Caso não tenha digitado, pedir para o usuário digitar novamente.

# Início do loop
while True:

# Solicita um número inteiro ao usuário
    numero = input("Informe, por gentileza, um número inteiro:") 

# Verifica se a string inserida é um número inteiro
    if numero.isnumeric(): 
    
 # Exibe na tela o número inteiro inserido pelo usuário
        print("O numero digitado foi: ", numero) 
        # Encerra o loop
        break

# Se a string inserida não for um número inteiro, exibe uma mensagem de erro.
    else: 
        print("O número não é inteiro.") 

