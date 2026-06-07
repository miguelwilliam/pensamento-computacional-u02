entrada = [int(x) for x in input().split(' ')]
N = entrada.pop(0)

resultados = []
for i in range(N):
    X = entrada[i*2]
    Y = entrada[i*2+1]
    resultado = 0

    if X % 2 == 0: # SE PAR
        for j in range(Y):
            # print(f'{X} PAR: + {X+1+2*j}')
            resultado += X+1+2*j
    
    else: # SE IMPAR
        for j in range(Y):
            # print(f'{X} ÍMPAR: + {X+1+2*j}')
            resultado += X+2*j
    
    resultados.append(resultado)

print(*resultados)