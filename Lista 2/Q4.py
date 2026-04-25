P = float(input('Peso: '))
A = float(input('Altura: '))
imc = P/A**2

if imc >= 30:
    print('Obesidade')
elif imc >= 25:
    print('Sobrepeso')
elif imc >= 18.5:
    print('Peso normal')
else:
    print('Abaixo do peso')