# i = 0
# while i < 5:
#     print(i)
#     i += 1


# for i in range(5):
#     print (i)

# contagem = 0
# while contagem < 5:
#     print(contagem)
#     contagem += 1


# x = "global"
# #loop for para alterar duas vezes
# if i == 0:
#     y = 'local na primeira ieração'
# else:
#     y = 'local na segunda iteração'
# print(f'iteração{i+1}')
# print(f'X:{x}')# pode acessar x
# print(f'X:{y}')# pode acessar y ; pois esta definida como loop

# num = int(input("Digite o mulltiplicador: "))
# for i in range(11):
#     i *= num
#     print (i)


# num = int(input("Digite o número para ver a tabuada: "))
# cont = 1
# while cont <= 10:
#     print(f"{num} x {cont} = {num * cont}")
#     cont += 1


# import random

# numero = random.randint(1, 10)
# print("Número aleatório:", numero)


import random

numero = random.randint(1, 50)
palpite = 0
tentativas = 0

while palpite != numero:
    palpite = int(input("Adivinhe um número entre 1 e 50: "))
    tentativas += 1

    if palpite < numero:
        print("Tente um número maior.")
    elif palpite > numero:
        print("Tente um número menor.")

print("Você acertou!")
print("Tentativas:", tentativas)