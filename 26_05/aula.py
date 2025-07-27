# Python não dispõe de um SWITCH nativo, mas você pode
# usar um dicionário para simular esse comportamento:

#exemplo

# Exemplo simples de dias da semana
def switch_dia(dia):
    dias = {
        1: "Segunda-feira",
        2: "Terça-feira",
        3: "Quarta-feira",
        4: "Quinta-feira",
        5: "Sexta-feira",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(dia, "Dia inválido")

dia_selecionado = switch_dia(3)
print("O dia é:", dia_selecionado)

#############################################################################################################

# Funções para simular comandos
def acender_luzes():
    return "Luzes acesas"

def ajustar_termostato(temperatura):
    return f"Termostato ajustado para {temperatura} graus"

def tocar_musica(musica):
    return f"Tocando {musica}"

def comando_nao_encontrado(*args):
    return "Comando não reconhecido"

# Dicionário simulando SWITCH
comandos = {
    "acender luzes": acender_luzes,
    "ajustar termostato": ajustar_termostato,
    "tocar música": tocar_musica
}

# Função para processar comandos
def processar_comando(comando, *args):
    acao = comandos.get(comando, comando_nao_encontrado)
    return acao(*args)

# Exemplo de uso
print(processar_comando("acender luzes"))
print(processar_comando("ajustar termostato", 22))
print(processar_comando("tocar música", "Beethoven"))
print(processar_comando("abrir portas"))

###########################################################################################
def processar_texto(texto):
    return texto.upper()
def processar_numero(numero):
    return numero * 2
def padrao():
    return "Opção inválida"
switch = {
"texto": processar_texto,
"numero": processar_numero
}
# Exemplo de uso
entrada = "texto"
valor = "Olá Mundo"
resultado = switch.get(entrada,padrao)(valor)
print(resultado) # Saída: Olá mundo

############################################################################################

# Podemos combinar SWITCH com loops para processar uma lista
# de tarefas ou dados de diferentes tipos. Vejamos um exemplo:
tarefas = [
("texto", "Olá"),
("numero", 10),
("desconhecido", None)
]
for tipo, valor in tarefas:
    resultado1 = switch.get(tipo, padrao)(valor)
    print(f"Resultado: {resultado1}")

#############################################################################################
""""""
# Imagine um sistema de processamento de comandos no qual cada
# comando deve ser executado de forma diferente.
# Vamos criar uma simulação:
# Imagine um sistema de processamento de comandos no qual cada
# comando deve ser executado de forma diferente.
# Vamos criar uma simulação:

def adicionar_usuario(dados):
    # Lógica para adicionar um usuário
    return f"Usuário {dados['nome']} adicionado."

def remover_usuario(dados):
    # Lógica para remover um usuário
    return f"Usuário {dados['nome']} removido."

def padrao(dados):
    return "Comando não reconhecido."

# Dicionário de comandos
comandos = {
    "adicionar": adicionar_usuario,
    "remover": remover_usuario
}

# Exemplo de uso em um sistema
comando_entrada = {
    "tipo": "adicionar",
    "dados": {"nome": "João"}
}

comando = comando_entrada["tipo"]
dados = comando_entrada["dados"]

resultado = comandos.get(comando, padrao)(dados)

print(resultado)  # Saída: Usuário João adicionado.


### tarefa da semama 13 (ENVIAR AO AVA)

# Uma empresa de e-commerce processa diferentes tipos de solicitações de clientes (ex: fazer pedido,
# devolver produto, atualizar dados). Atualmente, o sistema usa muitos if, elif, else,
# o que dificulta a manutenção do código. Você deve propor uma solução melhor usando dicionário + 
# funções em Python, simulando o comportamento de um switch.


# DICAS

# Passos para simular um switch em Python usando dicionário e funções:

# 1. Explique o problema:
# O sistema atual usa muitos blocos if/else, o que torna o código confuso e difícil de manter.

# 2. Crie funções para cada tipo de solicitação:
# Exemplo:
# def fazer_pedido(dados): return f"Pedido feito por {dados['nome']}"
# def devolver_produto(dados): return f"Produto devolvido por {dados['nome']}"
# def atualizar_dados(dados): return f"Dados atualizados para {dados['nome']}"
# def comando_nao_reconhecido(dados): return "Comando inválido."

# 3. Monte um dicionário que associa o nome do comando à função correspondente:
# comandos = {
#     "pedido": fazer_pedido,
#     "devolucao": devolver_produto,
#     "atualizar": atualizar_dados
# }

# 4. Crie uma entrada simulada:
comando_entrada = {"tipo": "pedido", "dados": {"nome": "João"}}

# 5. Use o método .get() para buscar e executar a função correta:
comando = comando_entrada["tipo"]
dados = comando_entrada["dados"]
funcao = comandos.get(comando, comando_nao_reconhecido)
print(funcao(dados))  # Saída esperada: Pedido feito por João

# 6. Vantagens dessa abordagem:
# - Código mais limpo e organizado
# - Mais fácil de manter e entender
# - Permite adicionar novos comandos com facilidade

# 7. Conclusão:
# O uso de dicionário com funções simula bem o switch case em Python,
# sendo uma alternativa prática e eficiente para sistemas com muitos comandos diferentes.

#############################################################################################################

#EXEMPLO DE BOAS PRATICOS
def calcular_preco(cafe):
    precos = {
        "espresso": 1.50,
        "latte": 2.00,
        "cappuccino": 2.25
    }
    return precos.get(cafe, "Café não disponível")

# Exemplo de uso
preco = calcular_preco("espresso")
print(preco)


