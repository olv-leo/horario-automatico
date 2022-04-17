from itertools import combinations

# DISPONIBILIDADES DE TODAS AS MATERIAS 1 = DISPONIBILIDADE 2 = PREFERENCIA

materias = {
    'Africanidades': [0, 0, 1, 2, 2],
    'Álgebra': [0, 0, 0, 1, 0],
    'Bio - Ecossistemas': [0, 0, 1, 0, 0],
    'Bio - Organismos': [0, 0, 0, 0, 2],
    'Filosofia': [0, 0, 0, 1, 2],
    'Física 1': [0, 0, 0, 1, 0],
    'Física 2': [0, 2, 0, 0, 0],
    'Geografia': [2, 1, 0, 1, 1],
    'Geografia': [0, 2, 0, 1, 0],
    'Geometria': [1, 2, 1, 0, 0],
    'História': [2, 0, 1, 1, 0],
    'História': [0, 0, 1, 0, 0],
    'Matemática PBL': [1, 2, 0, 0, 0],
    'Química da Vida': [0, 0, 0, 0, 2],
    'Química Geral': [2, 2, 0, 0, 0],
    'Sociologia': [0, 0, 0, 2, 0],
    'Texto 1': [2, 0, 1, 0, 0],
    'Texto 1': [0, 0, 1, 2, 0],
    'Texto 2': [2, 1, 0, 0, 0],
    'Tratamento de Informação': [0, 1, 0, 0, 2]
}

disponibilidades = {
    'segunda': [],
    'terca': [],
    'quarta': [],
    'quinta': [],
    'sexta': []
}

# COLOQUEI OS INDICES DAS DISCIPLINAS DISPONIVEIS EM CADA UM DOS VETORES (EX: NO VETOR DA SEGUNDA ESTÃO OS INDICES DE TODAS AS DISCIPLINAS QUE TEM DISPONIBILIDADE
# NA SEGUNDA)
for materia, disponibilidade in materias.items():
    if disponibilidade[0] >= 1:
        disponibilidades['segunda'].append(materia)

    if disponibilidade[1] >= 1:
        disponibilidades['terca'].append(materia)

    if disponibilidade[2] >= 1:
        disponibilidades['quarta'].append(materia)

    if disponibilidade[3] >= 1:
        disponibilidades['quinta'].append(materia)

    if disponibilidade[4] >= 1:
        disponibilidades['sexta'].append(materia)

for dia, materia in disponibilidades.items():
    print(f'{dia}: {materia}')


# CRIEI UM VETOR PARA CADA DIA DA SEMANA PARA ARMAZENAR TODAS AS COMBINACOES DE DISCIPLINAS POSSIVEIS NAQUELE DIA
possibilidadessegunda = []
possibilidadesterca = []
possibilidadesquarta = []
possibilidadesquinta = []
possibilidadessexta = []

horario01 = []
horario02 = []
horario03 = []
horario04 = []

materias_por_dia = {
    'segunda': [],
    'terca': [],
    'quarta': [],
    'quinta': [],
    'sexta': []
}

# FIZ TODAS AS COMBINAÇÃO POSSIVEIS PARA TODOS OS DIAS DA SEMANA BASEADA NAS DISPONIBILIDADES DOS PROFESSORES
for conjunto_de_materias in combinations(disponibilidades['segunda'], 4):
    materias_por_dia['segunda'].append(conjunto_de_materias)


"""
for i in itertools.combinations(disponibilidadeterca, 4):
    possibilidadesterca += [i]

for i in itertools.combinations(disponibilidadequarta, 4):
    possibilidadesquarta += [i]

for i in itertools.combinations(disponibilidadequinta, 4):
    possibilidadesquinta += [i]

for i in itertools.combinations(disponibilidadesexta, 4):
    possibilidadessexta += [i]

segundaterca = []
segundaterca01 = []

segundatercaquarta = []
segundatercaquarta01 = []

segundatercaquartaquinta = []
segundatercaquartaquinta01 = []

segundatercaquartaquintasexta = []
segundatercaquartaquintasexta01 = []

# SEGUNDA E TERÇA
for i in range(len(possibilidadessegunda)):
    for n in range(len(possibilidadesterca)):
        novo = [possibilidadessegunda[i] + possibilidadesterca[n]]
        segundaterca += novo

for i in range(len(segundaterca)):
    if len(segundaterca[i]) == len(set(segundaterca[i])):
        segundaterca01 += [segundaterca[i]]

# SEGUNDA, TERÇA E QUARTA
for i in range(len(segundaterca01)):
    for n in range(len(possibilidadesquarta)):
        novo = [segundaterca01[i] + possibilidadesquarta[n]]
        segundatercaquarta += novo

for i in range(len(segundatercaquarta)):
    if len(segundatercaquarta[i]) == len(set(segundatercaquarta[i])):
        segundatercaquarta01 += [segundatercaquarta[i]]

# SEGUNDA, TERÇA, QUARTA E QUINTA
for i in range(len(segundatercaquarta01)):
    for n in range(len(possibilidadesquinta)):
        novo = [segundatercaquarta01[i] + possibilidadesquinta[n]]
        segundatercaquartaquinta += novo

for i in range(len(segundatercaquartaquinta)):
    if len(segundatercaquartaquinta[i]) == len(set(segundatercaquartaquinta[i])):
        segundatercaquartaquinta01 += [segundatercaquartaquinta[i]]

# SEGUNDA, TERÇA, QUARTA, QUINTA E SEXTA
for i in range(len(segundatercaquartaquinta01)):
    for n in range(len(possibilidadessexta)):
        novo = [segundatercaquartaquinta01[i] + possibilidadessexta[n]]
        segundatercaquartaquintasexta += novo

for i in range(len(segundatercaquartaquintasexta)):
    if len(segundatercaquartaquintasexta[i]) == len(set(segundatercaquartaquintasexta[i])):
        segundatercaquartaquintasexta01 += [segundatercaquartaquintasexta[i]]

# DA NOTA PARA CADA UM DOS HORÁRIOS A PARTIR DA PREFERÊNCIA DOS PROFESSORES
possibilidades = []
for i in range(len(segundatercaquartaquintasexta01)):
    a = 0
    for j in range(0, 4):
        a += disponibilidadepormateria[int(segundatercaquartaquintasexta01[i][j])][0]
    for j in range(4, 8):
        a += disponibilidadepormateria[int(segundatercaquartaquintasexta01[i][j])][1]
    for j in range(8, 12):
        a += disponibilidadepormateria[int(segundatercaquartaquintasexta01[i][j])][2]
    for j in range(12, 16):
        a += disponibilidadepormateria[int(segundatercaquartaquintasexta01[i][j])][3]
    for j in range(16, 20):
        a += disponibilidadepormateria[int(segundatercaquartaquintasexta01[i][j])][4]
    possibilidades += [((segundatercaquartaquintasexta01[i]), (a))]
possibilidades.sort(key=lambda x: x[1])

print('O melhor horário encontrado foi:')
print('SEGUNDA-FEIRA')
for i in range(0, 4):
    print(nomematerias[possibilidades[(len(possibilidades) - 1)][0][i]])
print(' ')

print('TERÇA-FEIRA')
for i in range(4, 8):
    print(nomematerias[possibilidades[(len(possibilidades) - 1)][0][i]])
print(' ')

print('QUARTA-FEIRA')
for i in range(8, 12):
    print(nomematerias[possibilidades[(len(possibilidades) - 1)][0][i]])
print(' ')

print('QUINTA-FEIRA')
for i in range(12, 16):
    print(nomematerias[possibilidades[(len(possibilidades) - 1)][0][i]])
print(' ')

print('SEXTA-FEIRA')
for i in range(16, 20):
    print(nomematerias[possibilidades[(len(possibilidades) - 1)][0][i]])
print(' ')
"""
