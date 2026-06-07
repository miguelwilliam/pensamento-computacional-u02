maior_gasto = None

print('Informe os gastos no dia:')
while True:
    gasto = float(input())
    if gasto == 0: break
    if maior_gasto == None:
        maior_gasto = gasto
        continue
    if gasto > maior_gasto:
        maior_gasto = gasto

if maior_gasto != None:
    print(f'O seu maior gasto hoje foi R$ {maior_gasto:.2f}')
else:
    print('Você não teve gastos hoje!')