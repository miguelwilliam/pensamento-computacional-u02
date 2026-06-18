N = int(input('Qual o N? '))
print('Digite os valores:')

valores = []
operacoes = ['+', '*']
resultado = 0

for i in range(N):
    valores.append(int(input()))

op = int(input('Qual a op? '))
A = int(input('Qual o A? '))
B = int(input('Qual o B? '))


if op == 0:
    resultado = valores[A-1]+valores[B-1]
elif op == 1:
    resultado = valores[A-1]*valores[B-1]

print(f'{valores[A-1]} {operacoes[op]} {valores[B-1]} = {resultado}')