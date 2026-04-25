print('Insira a taxa do exame para 10 pacientes:')
taxas = []
for i in range(10):
    taxas.append(int(input()))

media_aritmetica = sum(taxas)/10
media_geometrica = 1
media_harmonica = 0

for taxa in taxas:
    media_geometrica = media_geometrica*taxa
    media_harmonica += 1/taxa

media_geometrica = media_geometrica**(1/10)
media_harmonica = 10/media_harmonica


erro_harmonica = (media_harmonica-media_aritmetica)/media_aritmetica
erro_geometrica = (media_geometrica-media_aritmetica)/media_aritmetica
erro_medio = (erro_harmonica+erro_geometrica)/2

print(f'Média aritmética: {media_aritmetica:.2f}')
print(f'Média harmônica: {media_harmonica:.2f}')
print(f'Média geométrica: {media_geometrica:.2f}')
print(f'Erro médio: {erro_medio*100:.2f}%')