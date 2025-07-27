# conceitos novos semana 9

letra = input("Digite uma letra do alfabeto: ")
# Converte a letra em minúscula para evitar problemas
#letra = letra.lower()
# Converte a letra em maiuscula para evitar problemas
letra = letra.upper()

# conceitos novos semana 10

#for
# Estrutura de Repetição : For (para)
# Itera sobre uma sequência (lista, range, string, etc)

for i in range(1, 6):  # range(1,6) gera números de 1 a 5
    print("Número:", i)

#usado quando se sabe previamente o numero de passos
#que o loop ira fazer

#while
# Estrutura de Repetição: While (enquanto)
# Executa o bloco enquanto a condição for verdadeira
contador = 1

while contador <= 5:
    print("Contador =", contador)
    contador += 1 

# Estrutura de Repetição: Loop infinito com condição de saída
while True:
    comando = input("Digite 'sair' para terminar: ")
    if comando.lower() == "sair":
        print("Programa encerrado.")
        break
    else:
        print("Você digitou:", comando)

# usado quando não se saber quantos passos o loop ira percorrer

# conceitos semana 11

# como descobrir se um numero é impar ou par
# Solicita que o usuário digite um número
numero = int(input("Digite um número: "))
 # Verifica se o número é par ou ímpar
if numero % 2 == 0:
 print("O número é par")
else:
 print("O número é ímpar")

# como descobrir se um numero é positivo
num = int(input("Digite um numero: "))
if num > 0 :print("numero é positivo")

# o uso de expressoes condicionais em estruturas de decisão e AND,OR ou NOT

#OR true , false = true
#AND true , true = true
#NOT true = false
dia = "Domingo"
if dia == "Sábado" or dia == "Domingo":
 print("Hoje é dia de descanso.")
else:
   print("Hoje é dia útil.")



# a importancia do codigo estar alinhado corretamente para o interpretador python conseguir ler o codigo
dia = "Domingo"
if dia == "Sábado" or dia == "Domingo":
print("Hoje é dia de descanso.")
else:
print("Hoje é dia útil.")


# conceitos semana 12

# Programa para verificar aprovação de alunos e listar notas válidas

# bonecas russas 

# Lista com notas dos alunos
notas = [8.5, 7.0, 4.5, 9.0, -1, 10]

# Percorre cada nota da lista
for nota in notas:
    # Verifica se a nota é válida (entre 0 e 10)
    if 0 <= nota <= 10:
        print(f"Nota válida: {nota}")
        
        # Verifica se o aluno foi aprovado (nota >= 7)
        if nota >= 7:
            print("Status: Aprovado")
        else:
            print("Status: Reprovado")
    else:
        # Caso a nota seja inválida, exibe mensagem de erro
        print(f"Nota inválida: {nota}")

print("Fim da verificação.")
