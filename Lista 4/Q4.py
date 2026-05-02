pontuacoes = []
print('Informe as pontuações dos atletas. Digite -1 para encerrar')
while True:
    p  = int(input())
    if p == -1:
        break
    pontuacoes.append(p)

recorde = sorted(pontuacoes)[-1]

print(f'O recorde de pontos é {recorde}.')
