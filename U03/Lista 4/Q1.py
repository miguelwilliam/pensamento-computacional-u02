N = int(input('Qual o valor de N? '))
valores = []
print('Digite os valores:')
for i in range(N):
    valores.append(int(input()))

def getDivisores(n:int):
    divisores = []
    for i in range(n):
        if n % (i+1) == 0:
            divisores.append(i+1)
    return divisores

for val in valores:
    divs = getDivisores(val)
    if len(divs) == 2:
        print(f'{val} é primo')
    else:
        print(f'{val} não é primo, os divisores são: {divs}')