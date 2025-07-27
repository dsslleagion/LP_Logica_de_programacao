numero_candidato = int(input('Digite o numero do seu candidato:'))

Candidato1_numero = 1
Candidato1_partido = "milaasenpaii"
Candidato1_nome = "Camila"
Candidato1_vice = "Isadora"

Candidato2_numero = 2
Candidato2_partido = "insuportaveis"
Candidato2_nome = "Jessica"
Candidato2_vice = "ana"


if numero_candidato == Candidato1_numero:
    print("candidato:", Candidato1_nome)
    print("partido:",Candidato1_partido)
    print("vice-prefeito:", Candidato1_vice)
elif numero_candidato == Candidato2_numero:
    print( "candidato:",Candidato2_nome  )
    print("partido:", Candidato2_partido)
    print("vice-prefeito:",Candidato2_vice )
else:
    print("candidato não encontrado")