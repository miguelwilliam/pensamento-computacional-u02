def par(n:int):
    return n % 2

soma_pares = 0
for i in range(4):
    N = int(input(f'Digite número {i+1}: '))
    if par(N) == 0:
        soma_pares += N

print(f'Soma dos números pares: {soma_pares}')