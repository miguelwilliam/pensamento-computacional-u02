N = int(input())

M = []

for linha in range(N):
    col_atual = []

    for col in range(N):
        if linha == 0: # CASO DE LINHA INICIAL
            col_atual.append(col+1)

        elif linha == N-1: # CASO DE LINHA FINAL
            col_atual.append(N-col)

        else: # CASO DE LINHA ENTRE
            n_atual = M[linha-1][col]-1
            try:
                if M[linha-1][col] > M[linha-2][col] or  M[linha-1][col] == 1:
                    n_atual += 2
            except:
                pass
            
            col_atual.append(n_atual)

    M.append(col_atual)

for i in M:
    print(i)