n = int(input('Qual o número de pessoas? '))
idades = 0

print('Informe as idades:')
for i in range(n):
    idades += int(input())

print(f'A média de idade das pessoas é {int(idades/n)} anos')