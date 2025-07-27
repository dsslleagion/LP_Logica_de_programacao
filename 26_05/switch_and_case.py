# Exercício: Simulação do Switch-Case em Python
# Objetivo: Mostrar a estação do ano conforme o número digitado

# Solicita um número ao usuário
numero = int(input("Digite um número de 1 a 4 para saber a estação do ano: "))

# Usa if, elif e else para simular um switch-case
if numero == 1:
    print("Verão")         # Caso o número seja 1
elif numero == 2:
    print("Outono")        # Caso o número seja 2
elif numero == 3:
    print("Inverno")       # Caso o número seja 3
elif numero == 4:
    print("Primavera")     # Caso o número seja 4
else:
    # Se o número for diferente de 1 a 4
    print("Opção inválida")


# -------------------------
# RESUMO:
# Python não tem switch case nativo (como em outras linguagens).
# A alternativa mais comum é usar if...elif...else.
# Cada elif funciona como um "case".
# O else funciona como o "default" (quando nenhum caso é verdadeiro).


# Exemplo simples de "switch case" em Python usando dicionário

# Suponha que o usuário forneça um número de 1 a 7
dia = 3

# Criamos um dicionário onde as chaves são os casos (como o case no switch)
dias_semana = {
    1: "Domingo",         # case 1
    2: "Segunda-feira",   # case 2
    3: "Terça-feira",     # case 3
    4: "Quarta-feira",    # case 4
    5: "Quinta-feira",    # case 5
    6: "Sexta-feira",     # case 6
    7: "Sábado"           # case 7
}

# Usamos o método get() para simular o switch:
# Se o número existir, retorna o dia; se não, mostra mensagem de erro
print(dias_semana.get(dia, "Número inválido. Use um número de 1 a 7."))

# -------------------------
# RESUMO:
# Python não tem switch case como outras linguagens.
# Podemos usar dicionário para simular isso de forma simples.
# A função .get(chave, valor_padrao) ajuda a lidar com casos inválidos.

