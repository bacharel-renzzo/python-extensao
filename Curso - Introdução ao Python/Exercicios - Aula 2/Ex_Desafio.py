# Desafio - Gasolina

# Import da biblioteca random - radint
from random import randint

## Declaração de Variáveis

qtd_litros = randint(1,52)
gas_valor = 5.50
alc_valor = 4.80

# Solicitando ao usuário para que informe o tipo do abastecimento
tipo = input("Informe (A) para álcool ou (G) para gasolina: ".lower())

# Declaração de If
if tipo =="A":
    if qtd_litros <=20:
        total = qtd_litros * alc_valor * (1-0.03)
        print("Total a pagar em reais: ", total)
# Declaração de Else
    else:
        total = qtd_litros * alc_valor * (1-0.05)
        print("Total a pagar em reais:  ", total)

# Declaração de If
elif tipo == "B":
    if qtd_litros <= 20:
        total = qtd_litros * gas_valor * (1-0.04)
        print("Total a pagar em reais: ", total)
# Declaração de Else
    else:
        print("Opção Inválida")


