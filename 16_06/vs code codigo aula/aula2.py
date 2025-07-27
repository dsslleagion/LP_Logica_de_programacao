# sintaxe do FOR 

# sequência, como listas , strings, tuplas , objetos

#for variavel in sequencia:

#for passo in sequencia
for i in range(1,11):
    print(f"{i}:Vai se lascar")

palavras = "cuzinho"
for letras in palavras:
    print(letras)

# arrays ou listas
lista_filmes = ["rapunzel","zootopia","pequenino","duro de matar","gente grande","Fast and furious 3","Gigantes de Aço"]
              #  0       ,    1      , 2         ,  3             , 4 
for i in lista_filmes:
    print(i)


# dicionario 
lista_filmes_dic = {
    "corrida":"fast and furious",
    "Si-fi":"Transformers",
    "aventura":"Star wars 1",
    "ação":"Deadpool 3",
    "terror":"Pânico 1"
}
for genero,filme in lista_filmes_dic.items():
    print(f"o gênero do filme é: {genero} e o nome é:{filme}")


for i in "tamarindo":
    print(i)

#fluxo (inicio, condição, incremento)
for i in range():
    print(i)




#banco de dados
usuarios = {"nome":"Ryan","idade":"2000"}#JSON
for chave,valor in usuarios.items():
    print(f"{chave}: {valor}")


#banco de dados
usuarios = [{"nome":"Ryan","idade":"2000"},{"nome":"Jeferson","idade":"10 A.C " }]#JSON
for item in usuarios:
    print(f"{item["nome"]} tem {item["idade"]} anos")


numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)