print('Digite um número:')
n = int(input())

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n=(n-1))

if n == 0:
    print('O número deve ser maior que 0.')
else:
    print(f'Resultado do fatorial: {fatorial(n=n)}')