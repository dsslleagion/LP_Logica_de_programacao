# Tarefa da semana 9

# Construir um programa em Python que permita
# a interpretação, em código, de letras do
# alfabeto.

# letra = input("Digite uma letra do alfabeto: ")

# # upper ou o lower 
# letra = letra.lower()

# if letra == 'a':
#     print("avião")
# elif letra == 'b':
#     print("Bola")
# elif letra == 'c':
#     print("cebola")
# elif letra == 'd':
#     print("Dionisio")
# else:
#     print("Não conheço uma palavra que comece com essa letra")



# tarefa da semana 10

# 1.	Crie um programa que exiba uma tabela de multiplicação para um número fornecido pelo usuário. 
# Utilize o laço for para iterar de 1 a 10 e imprimir o produto do número fornecido com cada um desses valores. 

# Orientações:
# •	Peça ao usuário para inserir um número;
# •	Use um laço for para percorrer um intervalo de 1 a 10;
# •	Em cada iteração, calcule o produto do número fornecido pelo valor atual do laço;
# •	Imprima cada produto em uma nova linha.

# numero = int(input("Digite um numero para ver sua tabuada: "))

# print(f"\nTabuada do numero {numero}:")
# for i in range(1, 11):
#     produto = numero * i
#     print(f"{numero}x {i}={produto}")




# 2.	Desenvolva um programa que implemente um jogo de adivinhação de números. O programa deve
# gerar um número aleatório entre 1 e 50 e pedir ao usuário para adivinhar esse número. No entanto,
# o usuário tem um limite de 5 tentativas para acertar. O laço while deve ser usado para controlar
# as tentativas e fornecer feedback se o palpite está correto ou não. Se o usuário errar após 5 tentativas,
# o programa deve informar que o jogo acabou e revelar o número secreto.

# Orientações:
# •	Gere um número aleatório entre 1 e 50;
# •	Defina um limite de 5 tentativas para o usuário;
# •	Use um laço while para permitir que o usuário faça um palpite em cada iteração;
# •	Se o palpite estiver correto, informe ao usuário e encerre o laço;
# •	Se o palpite estiver incorreto, dê uma dica (maior ou menor) e continue o laço;
# •	Se o usuário não acertar em 5 tentativas, informe-o e revele o número secreto.

# import random
# # gerar o numero 
# numero_secreto = random.randint(1 , 50)
# tentativas = 0
# limite_tentativas = 5 

# print("Jogo de Adivinhação: Tente adivinhar o numero entre 1 a 50.")
# print(f"Você tem {limite_tentativas} tentativas.\n")

# while tentativas < limite_tentativas:
#     palpite = int(input(f"Tentativa {tentativas + 1}:"))
#     tentativas += 1

#     if palpite == numero_secreto:
#         print("Parabens! Você acertou o numero!")
#         break
#     elif palpite < numero_secreto:
#         print("Dica: O numero é Maior")
#     elif palpite > numero_secreto:
#         print("Dica: O numero é Menor")
#     else:
#         print(f"Tente denovo! ")
    
#     # if palpite != numero_secreto:
#     #     print(f"Tente denovo! O número era {numero_secreto}")



import random

# Gerar o número
numero_secreto = random.randint(1, 50)
tentativas = 0
limite_tentativas = 5

print("Jogo de Adivinhação: Tente adivinhar o número entre 1 e 50.")
print(f"Você tem {limite_tentativas} tentativas.\n")

while tentativas < limite_tentativas:
    palpite = int(input(f"Tentativa {tentativas + 1}: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("Dica: O número é maior.\n")
    elif palpite > numero_secreto:
        print("Dica: O número é menor.\n")


if palpite != numero_secreto:
    print(f"\nVocê perdeu! O número era {numero_secreto}.")
















