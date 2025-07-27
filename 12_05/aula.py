# verificar se um numero é positivo
num = int(input("digite um numero: "))
if num > 0: print("O número é positivo.")

# Verificar se um numero é par

num = int(input("Digite um numero: "))
if num % 2 ==0:print("O número é par.")


# #Código com identação correta 
# idade = int(input("Digite sua idade: "))
# if idade>= 18:
#     print("VocÊ é maior de idade.")
# else:
#     print("você é menor de idade")

# #-------------------------------------------

# #Codigo com indentação da incorreta
# if idade>= 18:
# print("VocÊ é maior de idade.")
# else:
# print("você é menor de idade")





idade = int(input("Digite sua idade: "))
classificacao_indicativa = 12
if idade >= classificacao_indicativa:
    print("Você pode assistir ao filme!")
else:
    print("Desculpe, você não pode assistir a esse filme.")


dia = "Domingo"
if dia == "Sábado" or dia == "Domingo":
 print("Hoje é dia de descanso.")
else:
   print("Hoje é dia útil.")


 # Solicita que o usuário digite a temperatura atual
temperatura = float(input("Digite a temperatura atual: "))
 # Verifica se a temperatura é maior que 30
if temperatura > 30:
 print("Está quente")
else:
 print("Está frio")





 # Solicita que o usuário digite um número
 numero = int(input("Digite um número: "))
 # Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")


 # Solicita que o usuário digite sua idade
idade = int(input("Digite sua idade: "))
 # Verifica se a idade é maior ou igual a 65
if idade >= 65:
 print("Você pode se aposentar")
else:
 print("Você ainda não pode se aposentar")


quantidade_de_itens = 0
valor_total = 0

if quantidade_de_itens > 5 and valor_total > 200:
 print("dar desconto")


nota_media=0
passou_no_exame_de_recuperacao=0

if nota_media > 7 or (nota_media > 5 and
passou_no_exame_de_recuperacao):
 print("Aluno passou")




 # Leitura das entradas do usuário
conectado = input("O usuário está conectado (sim/não)? ").lower()
amigo = input("O destinatário é um amigo (sim/não)? ").lower()
 # Verificação das condições e exibição da mensagem correspondente
if conectado == "sim" and amigo == "sim":
 print("Mensagem enviada")
else:
 print("Mensagem não enviada")


while i in range (10):
    print (i)
    i+=1




import random

#jogo de escolhas

shhh = random.randint(1,10)
tentativas = 0
limite = 5

while tentativas < limite:
    chute = int(input("advinhe o número escolhido: "))
    chute = int(chute)

    tentativas += 1

if chute > shhh:
    print("muito alto")
elif chute < shhh:
    print("muito baixo")
else:
    print("acertou")
    

if tentativas == limite and chute != shhh:
    print(f"Você perdeu! O número era {shhh}.")
    
