T = int(input())
for i in range(T):
    PA, PB, G1, G2 = [float(x) for x in input().split()]

    anos = 0
    while PA <= PB and not anos > 100:
        PA += int(PA*G1/100)
        PB += int(PB*G2/100)
        anos += 1
        # print(f'ANO {anos}: {PA} X {PB}')
    # print(f'ANO {anos}: {PA} X {PB} - FIM')

    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')