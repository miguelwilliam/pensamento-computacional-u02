N1 = float(input('Qual é a nota da primeira unidade? '))
N2 = float(input('Qual é a nota da segunda unidade? '))
N3 = float(input('Qual é a nota da terceira unidade? '))

nota_final = (N1*2+N2*3+N3*4)/9

if nota_final < 3:
    print('Francisco está reprovado')
elif nota_final < 7:
    print('Francisco está em prova final')
else:
    print('Francisco está aprovado')