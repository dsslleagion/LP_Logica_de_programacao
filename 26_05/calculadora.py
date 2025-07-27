# Desenvolva uma calculadora simples de 1 operador e 2 operandos.
# O usuario deve apresentar para o usuario as 4 operações basicas:

# + soma
# - subtração 
# * multiplicação 
# / divisão

# obtenção dos valores (Entrada)

print("Operadores: ")
print("+ - * /")
print("Digite o caracter de operacao:")
sinal = input()
while(sinal!='+' and sinal!="-" and sinal!="*" and sinal!="/"):
    print('\nOperador invalido! Digite novamente')
    print("+ - * /")
    sinal = input()
print('Digite o operado 1: ')
oper1 = float(input())
print('Digite o operado 2: ')
oper2 = float(input())
while(sinal=='/'and oper2==0):# tentativa de divisão por zero
    print("Tentativa de divisão por zero!")
    print("Digite o operação 2: ")
    oper2 = float(input())

# calculo da operação (PROCESSAMENTO)
resultado = 0.0 # variavel que armazena o resultado calculado
if(sinal == "+"):
    resultado = oper1 + oper2
elif(sinal == '-'):
    resultado = oper1 - oper2
elif (sinal == '*'):
    resultado = oper1 * oper2
elif (sinal == '/'):
    resultado = oper1 / oper2

#exibição da saida
print("\n "+str(oper1)+str(sinal)+str(oper2)+" = "+str(resultado))

