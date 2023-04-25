# Ex3 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

## Quantidade de itens vendidos por cada vendedor de uma loja/O quanto de bônus que ele irá receber

vendas = [100, 150, 1500, 2000, 120]
salarios = [1000, 1500, 2000, 2500, 1200]
bonus = []

## Calculo de bônus +  salário

for i in range(len(vendas)):
 if vendas[i] > 1000:
  bonus.append("Vendedor " + str(i+1))
salarios[i] *= 1.15

## Exibe ao usuário os vendedores que conseguiram os bônus

print("Os vendedores que conseguiram o bônus foram: ")
for v in bonus:
  print(v)