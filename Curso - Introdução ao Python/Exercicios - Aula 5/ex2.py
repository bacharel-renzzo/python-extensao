## Ex2 - Transcrever a mensagem do usuário de letras para números.

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

# Dicionário de conversão de letras para números
conversao = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

# Solicita ao usuário que digite uma mensagem
mensagem = input("Digite uma mensagem: ")

# Converte a mensagem em letras minúsculas e a percorre caractere por caractere
for caractere in mensagem.lower():

# Verifica se o caractere está presente no dicionário de conversão
    if caractere in conversao:

 # Se o caractere estiver no dicionário, exibe o número correspondente na tela
        print(conversao[caractere], end=' ')
 # Se o caractere não estiver no dicionário, exibe o próprio caractere na tela sem conversão
    else:
         print(caractere, end=' ')
