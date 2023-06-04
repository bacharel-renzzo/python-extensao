# Ex3 - Caluladora de Peso Ideal
## Fazer uma calculadora em que o usuário digita Altura em metros e Peso em quilos e se é do sexo biológico Masculino ou Feminino. O programa devolve ao usuário a informação qual seu peso ideal e quando precisa emagrecer para chegar lá. Ao final, o programa deve trazer uma frase motivadora para aqueles que estão acima do peso, frase parabenizando os que estão no peso ideal e uma outra frase de alerta aos que estão abaixo do peso. 

# Declarar a entrada da Altura
altura = float(input("Digite aqui a sua altura em metros: "))

# Declarar a entrada do Peso
peso = float(input("Digite aqui seu peso em quilos: "))

# Declarar a entrada do Sexo Biológico
sexo = input("Digite aqui seu sexo (M para Masculino e F para feminino): ")

# Declaração de if para calcular peso ideal
if sexo == "M":
    peso_ideal = (72.7 * altura) - 50
else:
    peso_ideal = (62.1 * altura) - 44.7

# Declarações finais
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
