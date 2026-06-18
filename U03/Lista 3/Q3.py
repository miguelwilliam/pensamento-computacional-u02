N = int(input('Quantos alunos? '))
alunos = []

print('Digite os nomes dos alunos:')
for i in range(N):
    alunos.append(input())

for i in range(len(alunos)//2):
    print(f'i = {i}')
    
    if (i+1) % 2 != 0:
        print(f'i é impar: {i+1}')
        continue
    
    print(f'i é par: {i+1}')
    print(f'Trocando os alunos: {alunos[i]}, {alunos[-(i+1)]}')
    alunos[i], alunos[-(i+1)] = alunos[-(i+1)], alunos[i]

print('Nova lista:')
for aluno in alunos:
    print(aluno)