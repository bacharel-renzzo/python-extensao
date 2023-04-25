# Ex1 - Escreva um programa que recebe 2 valores e devolve o maior entre eles.

# Declaração da variável 1
print("Informe, por gentileza, um número: ")
numero_um = float(input())

# Declaração da variável 2 
print("Informe, por gentileza, outro número: ")
numero_dois = float(input())

# Condição para imprimir na tela mensagem que o primeiro numero informado pelo usuário é o maior.
if(numero_um > numero_dois): 
    print("O número", numero_um, "é maior que o número", numero_dois)
   
# Condição para imprimir na tela mensagem que o segundo numero informado pelo usuário é o maior.
elif(numero_dois > numero_um):
    print("O número", numero_dois, "é maior que o número", numero_um)

# Else para informar para o usuário que o programa deu um erro. 
else: 
    print("Erro no Programa. Favor reiniciá-lo")
