convidados = ['Daniel', 'Aluizio', 'Isabel', 'Teles', 'Eduardo']
print('A lista contém os seguintes nomes:')
for nome in convidados: print(nome)

nome = input('Qual nome você quer verificar? ')
if nome in convidados: 
    print(f'O nome {nome} está na lista, acesso permitido!')
else:
    print(f'O nome {nome} não está na lista, acesso negado!')