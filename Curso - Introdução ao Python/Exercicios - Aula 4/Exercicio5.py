# Ex5 - Crie um programa que apagará todos os espaços de um texto.

# Solicita que o usuário insira um texto e armazena o valor na variável 'texto'
texto = input("Digite um texto: ") 

# Remove os espaços em branco do texto e armazena o valor na variável 'texto_sem_espacos'
texto_sem_espacos = texto.replace(" ", "") 

# Exibe o texto sem espaços em branco na tela
print("Texto sem espaços em branco:", texto_sem_espacos) 
