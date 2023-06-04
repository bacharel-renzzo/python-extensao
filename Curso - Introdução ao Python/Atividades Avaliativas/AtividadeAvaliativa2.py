"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 03/04/2023

"""

# Solicita a altura e o peso do usuário.

altura = float(input("Digite aqui a sua altura em metros: "))
peso = float(input("Digite aqui seu peso em quilos: "))
sexo = input("Digite aqui seu sexo (M para Masculino e F para feminino): ")

# Calcula o peso ideal de acordo com o sexo.

if sexo == "M":
    peso_ideal = (72.7 * altura) - 50
else:
    peso_ideal = (62.1 * altura) - 44.7

# Verifica se o usuário está acima ou abaixo do peso ideal para o sexo escolhido.

if peso < peso_ideal:
    diferenca = peso_ideal - peso
    mensagem = f"Você está abaixo do peso ideal para o seu sexo. Precisa engordar {diferenca} quilos."
    motivacao = "Não desanime. Com uma dieta balanceada e a prática de exercícios físicos, é possível chegar ao peso ideal."

elif peso > peso_ideal:
    diferenca = peso - peso_ideal
    mensagem = f"Você está acima do peso ideal para o seu sexo. Precisa emagrecer {diferenca} quilos."
    motivacao = "Não desanime. Com uma dieta balanceada e a prática de exercícios físicos, é possível chegar ao peso ideal."

else:
    mensagem = "Parabéns! Você está no peso ideal para o seu sexo"
    motivacao = "Continue praticando exercícios caso vocÊ pratique e mantenha a dieta caso deseja permanecer neste peso."

# Exibe o resultado para o usuário.

print("Seu peso ideal é: {peso_ideal} quilos.")
print(mensagem)
print(motivacao)             

