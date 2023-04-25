"""
Leia atentamente as perguntas do programa para obter a melhor experiência de tal.
Autor: Renzzo Silva Rocha
RA: 4231925318
Versão: 1.0
Data de criação: 21/04/2023

"""

carros = {"Chevrolet Tracker": 120, "Chevrolet Onix": 90, "Hyundai HB20": 85, "Hyundai Tucson": 120, "Fiat Uno": 60, "Fiat Mobi": 70, "Fiat Pulse": 130}

def verificar_estoque():
    print("Estoque:")
    for carro, valor in carros.items():
        print(f"{carro}: R${valor}/dia")

def retirar_veiculo(carro, dias):
    if carro in carros:
        valor_total = carros[carro] * dias
        del carros[carro]
        print(f"{carro} alugado por {dias} dias. Valor total: R${valor_total}")
    else:
        print(f"{carro} não encontrado no estoque")

def inserir_veiculo(carro, valor):
    if carro in carros:
        print(f"{carro} já está no estoque")
    else:
        carros[carro] = valor
        print(f"{carro} adicionado ao estoque por R${valor}/dia")

verificar_estoque()  
retirar_veiculo("Fiat Uno", 3)  
inserir_veiculo("Fiat Uno", 60)  