AL = float(input('Altura inicial de Levi: '))
TL = int(input('Taxa de Crescimento de Levi: '))
AH = float(input('Altura inicial de Hiago: '))
TH = int(input('Taxa de Crescimento de Hiago: '))
anos = 0

if AL > AH:
    print('Erro: Hiago deve ser maior que Levi inicialmente.')
elif TL < TH:
    print('Erro: A taxa de crescimento de Levi deve ser maior que a de Hiago.')
else:
    altura_atual_levi = AL
    altura_atual_hiago = AH

    while altura_atual_levi < altura_atual_hiago:
        anos += 1
        altura_atual_levi += (TL/100)
        altura_atual_hiago += (TH/100)

    print(f'Serão necessários {anos} anos para que Levi seja maior que Hiago.')