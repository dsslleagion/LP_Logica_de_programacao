#  Sintaxe do laço FOR.

#  O laço FOR em Python é uma estrutura de controle que viabiliza iterar sobre 
# sequências, como listas, strings, tuplas ou objetos iteráveis.

# Sintaxe básica:
 # for variavel in sequencia:
 # executa alguma ação

for i in range(1,6):
    print(i)


# Aqui, a variável é temporária e assume o valor de cada elemento da sequência a 
# cada iteração do laço. No código abaixo, a variável letra assume sucessivamente 
# os valores ‘P’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’ e, a cada iteração, imprime a letra atual


for letra in "python":
    print(letra)

#Fluxo de execução (início, condição, incremento)

for i in range(1, 10):  # range(3) gera 0, 1, 2
 print(i)

#  Aqui, i começa em 0 e incrementa em 1 a cada iteração até 
# que a sequência range(3) seja totalmente percorrida

# AGORA USO NO MERCADO DE TRABALHO MAIS COMPLEXO

# Iteração em dicionários
#  Útil para acessar chaves e valores em dicionários, 
# estruturas de dados fundamentais para armazenar e 
# processar informações de modo eficiente.

dados = {"nome": "Alice", "idade": 30}
for chave, valor in dados.items():
 print(f"{chave}: {valor}")

# Manipulação de dados em listas(arrays)

# Exemplo básico:
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
 print(numero)

#  Manipulação de dados complexos envolve lidar com estruturas 
# de dados como dicionários, listas de dicionários, JSON etc.
#  Exemplo:
dados = [{"nome": "Ana", "idade": 25}, {"nome": "Beto", "idade": 30}]
for item in dados:
 print(f"{item["nome"]} tem {item["idade"]} anos")

