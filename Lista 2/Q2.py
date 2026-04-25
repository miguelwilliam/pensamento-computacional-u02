valor_compra = int(input('Qual o valor da compra? '))
modo_pagamento = input('Como gostaria de pagar à vista(V) ou à prazo (P)? ')

if modo_pagamento == 'V':
    print(f'Valor à pagar: {valor_compra*0.95}')
elif modo_pagamento == 'P':
    print(f'Valor à pagar: {valor_compra*1.08}')
    for i in range(3):
        print(f'Parcela {i+1}: {(valor_compra*1.08)/3}')