import itertools

# DISPONIBILIDADES DE TODAS AS MATERIAS 1 = DISPONIBILIDADE 2 = PREFERENCIA
disponibilidadepormateria = [[0, 0, 1, 2, 2],  # AFRICANIDADES
                             [0, 0, 0, 1, 0],  # ÁLGEBRA
                             [0, 0, 1, 0, 0],  # BIO - ECOSSISTEMAS
                             [0, 0, 0, 0, 2],  # BIO - ORGANISMOS
                             [0, 0, 0, 1, 2],  # FILOSOFIA
                             [0, 0, 0, 1, 0],  # FÍSICA 1
                             [0, 2, 0, 0, 0],  # FÍSICA 2
                             [2, 1, 0, 1, 1],  # GEOGRAFIA
                             [0, 2, 0, 1, 0],  # GEOGRAFIA
                             [1, 2, 1, 0, 0],  # GEOMETRIA
                             [2, 0, 1, 1, 0],  # HISTÓRIA
                             [0, 0, 1, 0, 0],  # HISTÓRIA
                             [1, 2, 0, 0, 0],  # MATEMÁTICA PBL
                             [0, 0, 0, 0, 2],  # QUÍMICA DA VIDA
                             [2, 2, 0, 0, 0],  # QUÍMICA GERAL
                             [0, 0, 0, 2, 0],  # SOCIOLOGIA
                             [2, 0, 1, 0, 0],  # TEXTO 1
                             [0, 0, 1, 2, 0],  # TEXTO 1
                             [2, 1, 0, 0, 0],  # TEXTO 2
                             [0, 1, 0, 0, 2]]  # TRATAMENTO DE INFORMAÇÃO
nomematerias = ['Africanidades',
                'Álgebra',
                'Bio - Ecossistemas',
                'Bio - Organismos',
                'Filosofia',
                'Física 1',
                'Física 2',
                'Geografia',
                'Geografia',
                'Geometria',
                'História',
                'História',
                'Matemática PBL',
                'Química da Vida',
                'Química Geral',
                'Sociologia',
                'Texto 1',
                'Texto 1',
                'Texto 2',
                'Tratamento de Informação']

# CRIEI VETORES VAZIOS PARA CADA UM DOS DIAS DA SEMANA
disponibilidadesegunda = []
disponibilidadeterca = []
disponibilidadequarta = []
disponibilidadequinta = []
disponibilidadesexta = []

# COLOQUEI OS INDICES DAS DISCIPLINAS DISPONIVEIS EM CADA UM DOS VETORES (EX: NO VETOR DA SEGUNDA ESTÃO OS INDICES DE TODAS AS DISCIPLINAS QUE TEM DISPONIBILIDADE
# NA SEGUNDA)
for i in range(len(disponibilidadepormateria)):
    if disponibilidadepormateria[i][0] >= 1:
        disponibilidadesegunda += [i]

    if disponibilidadepormateria[i][1] >= 1:
        disponibilidadeterca += [i]

    if disponibilidadepormateria[i][2] >= 1:
        disponibilidadequarta += [i]

    if disponibilidadepormateria[i][3] >= 1:
        disponibilidadequinta += [i]

    if disponibilidadepormateria[i][4] >= 1:
        disponibilidadesexta += [i]

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

# FIZ TODAS AS COMBINAÇÃO POSSIVEIS PARA TODOS OS DIAS DA SEMANA BASEADA NAS DISPONIBILIDADES DOS PROFESSORES
for i in itertools.combinations(disponibilidadesegunda, 4):
    possibilidadessegunda += [i]
print(possibilidadessegunda)

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
