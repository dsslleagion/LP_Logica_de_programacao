def dias_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quartas-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira'
    }
    return dias.get(dia, "Dia invalido")

dia_selecionado = dias_semana(1)
print("O dia é:", dia_selecionado)