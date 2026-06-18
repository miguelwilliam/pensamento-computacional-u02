N = int(input('Quantidade de jogadores? '))
print('Digite os dados para cada jogador:')

dados = []

for i in range(N):
    dados_jogador = input().split()

    for i in range(len(dados_jogador)): # Corrigir os types
        try:
            dados_jogador[i] = int(dados_jogador[i])
        except:
            continue
    
    dados.append(dados_jogador)


pontos_saque = sum([d[4] for d in dados])/sum([d[1] for d in dados])*100
pontos_bloqueio = sum([d[5] for d in dados])/sum([d[2] for d in dados])*100
pontos_ataque = sum([d[6] for d in dados])/sum([d[3] for d in dados])*100

print(f'Pontos de Saque: {pontos_saque:.2f}%')
print(f'Pontos de Bloqueio: {pontos_bloqueio:.2f}%')
print(f'Pontos de Ataque: {pontos_ataque:.2f}%')