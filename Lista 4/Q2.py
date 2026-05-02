mes = int(input('Qual o número do mês? '))
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

if mes > len(meses):
    print(f'Erro: não existe mês de número {mes}! Por favor, digite um número entre 1 e 12.')
else:
    print(f'O mês é {meses[mes-1]}')