N = int(input('Quantos nomes? '))
alunos = []
for i in range(N):
    alunos.append(input())

print('Você digitou:')
for i in range(len(alunos)-1, -1, -1):
    print(alunos[i])