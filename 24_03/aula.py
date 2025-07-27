# idade = 20
# exame_medico = True
# violacao_transito = False
# if idade >= 18 and exame_medico and not violacao_transito:
#  print("Você pode solicitar sua carteira de motorista.")
# else:
#  print("Você não pode solicitar sua carteira de motorista.")



# best_seller = True
# lancado_ha_2_anos = False
# quantidade_livros = 4
# preco_livro = 50
# desconto = 0
# if best_seller or lancado_ha_2_anos:
#     desconto += 20
#     if quantidade_livros > 3:
#         desconto += 5
# preco_final = preco_livro * (1 - desconto / 100) * quantidade_livros
# print(f"O preço final após os descontos é de R$ {preco_final:.2f}.")


# idade = 30
# peso = 55
# gravida = False
# doou_90_dias = False
# if 16 <= idade <= 69 and peso >= 50 and not gravida and not doou_90_dias:
#  print("Você está apto para doar sangue!")
# else:
#  print("Infelizmente, você não está apto para doar sangue.")

# idade = 16
# acompanhada_adulto = True
# autorizacao_pais = False
# if idade >= 18 or (15 <= idade <= 17 and 
# (acompanhada_adulto or autorizacao_pais)):
#  print("Você pode assistir ao filme.")
# else:
#  print("Você não pode assistir ao filme.")

# gpa = 3.6
# top_10 = False
# voluntario_horas = 105
# if gpa >= 3.5 or top_10 or voluntario_horas > 100:
#     print("Você é elegível para a bolsa de estudos.")
# else:
#     print("Você não é elegível para a bolsa de estudos.")

# experiencia_python = 4
# experiencia_ml = 2
# diploma_mestrado = False
# if experiencia_python >= 3 and (experiencia_ml >= 2 or diploma_mestrado):
#  print("Você é elegível para a vaga.")
# else:
#  print("Você não é elegível para a vaga.")

# portfolio_forte = False
# audicao_excelente = True
# treinamento_previo_anos = 2
# if portfolio_forte or (audicao_excelente and treinamento_previo_anos >= 2):
#     print("Parabéns, você foi admitido na academia!")
# else:
#  print("Infelizmente, você não foi admitido na academia.")

# renda_mensal = 2500
# score_credito = 650
# fiador_score_credito = 680
# if renda_mensal >= 2000 and (score_credito >= 600 or fiador_score_credito >= 700):
#  print("Você é elegível para o empréstimo.")
# else:
#  print("Você não é elegível para o empréstimo.")

idade = input('digite sua idade')
exame_medico=input('passou em um exame?')
violacao_transito