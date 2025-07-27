# conceitos novos semana 11

texto = input("Digite um texto qualquer: ")

# Deixa todas as letras em maiúsculas
texto_maiusculo = texto.upper()
print("Texto em maiúsculo:", texto_maiusculo)


# Deixa todas as letras em minúsculas
texto_minusculo = texto.lower()
print("Texto em minúsculo:", texto_minusculo)

# Construir um programa em Python que permita
# a interpretação, em código, de letras do
# alfabeto.

letra = input("Digite uma letra do alfabeto: ")

# upper ou o lower 
letra = letra.lower()

if letra == 'a':
    print("avião")
elif letra == 'b':
    print("Bola")
elif letra == 'c':
    print("cebola")
elif letra == 'd':
    print("Dionisio")
else:
    print("Não conheço uma palavra que comece com essa letra")



