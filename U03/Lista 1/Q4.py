pontos = [int(x) for x in input().split()]
vertice1 = [pontos[0],pontos[1]]
vertice2 = [pontos[2],pontos[3]]

ponto = [pontos[4],pontos[5]]
if ponto[0] >= vertice1[0] and ponto[0] <= vertice2[0] and ponto[1] >= vertice1[1] and ponto[1] <= vertice2[1]:
    print('Dentro!')
else:
    print('Fora!')