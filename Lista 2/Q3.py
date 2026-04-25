print('Qual o número de pessoas? ')
p = int(input())
print('Informe as idades:')

soma_idades = 0
for i in range(p):
    soma_idades += int(input())

media = soma_idades/p
print(f'A média de idade das pessoas é {media:.1f} anos')