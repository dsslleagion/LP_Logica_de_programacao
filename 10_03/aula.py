# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade. Pode entrar.")
# else:
#     print("Você é menor de idade. Não pode entrar.")



# previsao = input("Qual é a previsão do tempo? (C = Chuva / S = Sem chuva): ")

# if previsao.upper() == "C":
#     print("Leve o guarda-chuva.")
# else:
#     print("Não é necessário levar o guarda-chuva.")




# # Solicita o cargo do funcionário
# cargo = input("Digite seu cargo: ")

# # Solicita se o funcionário tem permissão especial (convertendo para booleano)
# permissao_especial = input("Você tem permissão especial? (s/n): ").strip().lower() == 's'

# #Dica do final do codigo
# if condição:
#     print("Acesso permitido!")
# else:
#     print("Acesso negado.")

# # Solicita o cargo do funcionário
# cargo = input("Digite seu cargo: ")

# # Solicita se o funcionário tem permissão especial (convertendo para booleano)
# permissao_especial = input("Você tem permissão especial? (s/n): ").strip().lower() == 's'

# # Verifica as condições de acesso
# if cargo.lower() == "gerente" or permissao_especial:
#     print("Acesso permitido!")
# else:
#     print("Acesso negado.")








nome = input("digite seu nome:")













#AVA ex1
# Solicitar ao usuário que digite um número
# numero = float(input("Digite um número: "))

# Verificar se o número é positivo, negativo ou zero
# if numero > 0:
#     print("O número é positivo.")
# elif numero < 0:
#     print("O número é negativo.")
# else:
#     print("O número é zero.")

# AVA ex2

# Solicitar ao usuário que digite um número
#     numero =float (input("Digite um número: "))
# Verificar se o número é positivo, negativo ou zero
#     if numero > 0:
#         print ("O número é positivo.")
#     elif numero < 0:
#         print("O número é negativo.")
#     else:
#         print ("O número é zero.")

# AVA ex3
# valor_compra = float(input("Digite o valor da compra: ")) 
# if valor_compra >= 100: 
#     desconto = valor_compra * 0.1 
#     valor_final = valor_compra- desconto 
#     print("Parabéns! Você ganhou um desconto de 10%.") 
#     print("Valor final da compra: R$", valor_final) 
# else: 
#     print("Infelizmente, você não ganhou desconto.") 
#     print("Valor final da compra: R$", valor_compra)


# AVA ex4
# quantidade_desejada = int(input("Digite a quantidade desejada: "))
# if quantidade_desejada >= 10:
#  print("Produto disponível em estoque. Aproveite!")
# else:
#  print("Produto indisponível no momento. Volte mais tarde!")

# AVA ex5
#  nota_final = float(input("Digite a nota final: "))
#  if nota_final >= 7:
#     print("Parabéns! Você foi aprovado.")
#  else:
#     print("Infelizmente, você não foi aprovado. Estude mais e tente novamente!")

# Dica
# estoque = {"001": 10, "002": 0, "003": 5}

# codigo = input("Digite o código do produto: ")
# if codigo in estoque:
#     print(f"Quantidade disponível: {estoque[codigo]}" if estoque[codigo] > 0 else "Produto esgotado")
# else:
#     print("Código inválido")

# solução
# Lista de produtos em estoque (dicionário com código e quantidade)
# estoque = {
#     "001": 10,
#     "002": 0,
#     "003": 5,
#     "004": 2
# }

# Solicita o código do produto ao usuário
# codigo_produto = input("Digite o código do produto: ")

# Verifica se o código do produto está no estoque
# if codigo_produto in estoque:
#     quantidade = estoque[codigo_produto]
#     if quantidade > 0:
#         print(f"Produto disponível em estoque. Quantidade disponível: {quantidade}")
#     else:
#         print("Produto esgotado.")
# else:
#     print("Código de produto inválido.")


# AVA ex6
# idade = int(input("Digite a sua idade: "))
# if idade >= 18:
#     print("Você pode assistir ao filme.")
# else:
#     print("Desculpe, você não tem idade suficiente para assistir ao filme.")


