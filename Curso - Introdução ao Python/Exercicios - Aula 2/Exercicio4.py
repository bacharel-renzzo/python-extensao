# Ex4 - É triangulo ou Não é triângulo? 
# Para determinar se 3 segmentos de reta formam um triângulo, podemos fazer a verificação se a soma dos dois menores segmentos é maior do que o segmento maior.

# Declaração do primeiro segmento
print("Informe, por gentileza, o valor do primeiro segmento: ")
segmento_um = float(input())

# Declaração do segundo segmento
print("Informe, por gentileza, o valor do segundo segmento: ")
segmento_dois = float(input())

# Declaração do terceiro segmento
print("Informe, por gentileza, o terceiro número: ")
segmento_tres = float(input())

# Neste if, usar AND para avaliaar se o 1º segmento é o menor
if(segmento_um > segmento_dois and segmento_tres):
    print("o segmento um é o maior de todos os segmentos")
# Neste elif, usar AND para avaliaar se o 2º segmento é o maior
elif(segmento_dois > segmento_um and segmento_tres):
    print("O segmento dois é o maior de todos os segmentos")
# Neste elif, usar AND para avaliar se o 3º segmento é o maior
elif(segmento_tres > segmento_um and segmento_dois):
    print("O segmento três é o maior de todos os segmentos")
# Else para possíveis erros de digitação
else:
    print("Informe, por gentileza, um valor válido para o cálculo de todos os segmentos e identificação do maior.")

# Verificação se é triângulo e informar ao usuário.    
    if segmento_um < segmento_dois + segmento_tres and segmento_dois < segmento_um + segmento_tres and segmento_tres < segmento_um + segmento_dois:
        print("Os segmentos formam um triângulo.")

