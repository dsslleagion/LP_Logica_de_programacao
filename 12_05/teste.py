
import random

#jogo de escolhas

# shhh = random.randint(1,10)
# tentativas = 0
# limite = 5

# while tentativas < limite:
#     chute = int(input("advinhe o número escolhido: "))
#     chute = int(chute)

#     tentativas += 1

# if chute > shhh:
#     print("muito alto")
# elif chute < shhh:
#     print("muito baixo")
# else:
#     print("acertou")
    

# if tentativas == limite and chute != shhh:
#     print(f"Você perdeu! O número era {shhh}.")



import random

shhh = random.randint(1, 10)
tentativas = 0
limite = 5

while tentativas < limite:
    chute = int(input("Advinhe o número escolhido (1 a 10): "))
    tentativas += 1

    if chute == shhh:
        print(f"Acertou! Você precisou de {tentativas} tentativa(s).")
        break
    else:
        diferenca = abs(chute - shhh)
        if diferenca == 1:
            print("Está muito perto!")
        elif chute < shhh:
            print("Muito baixo.")
        else:
            print("Muito alto.")

if tentativas == limite and chute != shhh:
    print(f"Você perdeu! O número era {shhh}.")

