'''def compra(v, f):
    if f.lower() not in ['v', 'p']:
        print('Forma de pagamento inválida!')
        return

    if f.lower() == 'v':
        print(f'Valor à pagar: {int(v*0.95)}')
    elif f.lower() == 'p':
        print(f'Valor à pagar: {int(v*1.08)}')
        for i in range(3):
            print(f'Parcela {i+1}: {int((v*1.08)/3)}')

v = int(input('Qual o valor da compra? '))
f = input('Como gostaria de pagar: à vista (V) ou à prazo (P)? ')

compra(v=v, f=f)
'''
# =======================

def compra(v, f):
  if f.lower() not in ['v', 'p']:
    print('Forma de pagamento inválida!')
    return

  if f.lower() == 'v':
    print(f'Valor à pagar: {int(v*0.95)}')
  elif f.lower() == 'p':
    print(f'Valor à pagar: {int(v*1.08)}')
    for i in range(3):
      print(f'Parcela {i+1}: {int((v*1.08)/3)}')

v = int(input('Qual o valor da compra? '))
f = input('Como gostaria de pagar: à vista (V) ou à prazo (P)? ')

compra(v=v, f=f)