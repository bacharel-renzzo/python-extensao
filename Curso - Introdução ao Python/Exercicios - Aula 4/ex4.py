# Ex4 - Desenvolva uma calculadora de fatorial em que o usuário digita o número e o programa retorna seu fatorial.

# Solicita ao usuário que informe o número da tabuada que ele deseja
numero = int(input("Informe o número da tabuada que deseja ver (entre 1 e 10): "))

# Verifica se o número informado está dentro do intervalo permitido (entre 1 e 10)
if numero < 1 or numero > 10:
    print("Número inválido! Por favor, informe um número entre 1 e 10.")
else:
    print("Tabuada de", numero, ":")

 # Gera a tabuada do número informado
    for i in range(1, 11):
        print(numero, "X", i, "=", numero * i)