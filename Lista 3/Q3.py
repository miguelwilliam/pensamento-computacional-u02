valores = {
    '100': 5.5,
    '101': 15,
    '103': 20,
    '104': 18,
    '105': 6,
    }

pagamento = 0

running = True
while running:
    codigo = input('Digite o código do item: ')

    if codigo == '-1':
        break

    quantidade = int(input('Digite a quantidade: '))
    pagamento+=(quantidade*valores[codigo])

print(f'Total a pagar: R$ {pagamento:.2f}')