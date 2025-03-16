# Nesse exemplo, a condição do if não é 
# satisfeita (15 não é maior ou igual a 18), 
# então o programa verifica a condição 
# do elif.
#  Como 15 é menor que 18 e maior ou 
# igual a 13, a mensagem "Você é um 
# adolescente" é impressa

# idade = 15
# if idade >= 18:
#     print("Você é maior de idade.")
# elif idade < 18 and idade >= 13:
#     print("Você é um adolescente.")
# else:
#     print("Você é uma criança.")

# temperatura = 30
# if temperatura >= 30:
#     print("Vá à praia!")
# elif temperatura >= 20:
#     print("Um dia perfeito para um passeio no parque.")
# elif temperatura >= 10:
#     print("Que tal um filme em casa?")
# else:
#     print("Melhor ficar em casa, está muito frio lá fora.")

# temperatura = 30
# if temperatura < 0:
#   print("Muito frio")
# elif temperatura < 10:
#   print("Frio")
# elif temperatura < 20:
#   print("Ameno")
# elif temperatura < 30:
#   print("Quente")
# else:
#   print("Muito quente")

# nota = 85
# if nota >= 90:
#     print("A")
# elif nota >= 80:
#     print("B")
# elif nota >= 70:
#     print("C")
# elif nota >= 60:
#     print("D")
# else:
#     print("F")


# Solicita ao usuário o tempo de serviço em anos  
tempo_servico = int(input("Digite o tempo de serviço do colaborador (em anos): "))  

# Verifica se o tempo de serviço é menor ou igual a 5 anos  
if tempo_servico <= 5:  
    # Ação para colaboradores com até 5 anos de empresa  
    print("Aumento no vale-refeição")  

# Se não se encaixar na condição anterior, verifica se está entre 5 e 10 anos  
elif tempo_servico <= 10:  
    # Ação para colaboradores com mais de 5 e até 10 anos de empresa  
    print("Reajuste de 10% no salário")  

# Se não se encaixar nas condições anteriores, verifica se está entre 10 e 15 anos  
elif tempo_servico <= 15:  
    # Ação para colaboradores com mais de 10 e até 15 anos de empresa  
    print("Participação na festa de comemoração")  

# Caso o tempo de serviço seja maior que 15 anos  
else:  
    # Ação para colaboradores com mais de 15 anos  
    print("Nenhum benefício adicional aplicável")  
