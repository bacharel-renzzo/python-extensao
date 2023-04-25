# Ex2 - Faça um programa de verificação de login e senha. O usuário pode errar a senha até 3 vezes antes do programa terminar informando que o acesso foi bloqueado.

# Pede ao usuário que informe o seu login e sua senha

login = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Loop criado para demonstrar que o usuário perde o acesso caso erre a senha mais de 3 vezes.
tentativas_restantes = 2  

while senha != "senha_segura" and tentativas_restantes >= 0:
     print(f"Senha incorreta! Você tem mais {tentativas_restantes} tentativas.")
     if senha == "senha_segura":
      print("Acesso permitido!")
     else:
      print("Acesso bloqueado.")
      break

 # Pede ao usuário que informe a senha novamente, decrementando uma tentativa a cada erro de senha.    

senha = input("Digite a senha novamente: ")
tentativas_restantes -= 1


