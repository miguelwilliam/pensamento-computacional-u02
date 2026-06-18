def checarPositivoNaoNulo(n:int):
    if n > 0:
        return True
    return False

def piramide(n:int):
    if checarPositivoNaoNulo(n=n) == False:
        print('Valor invalido!')
        return
    
    for i in range(n):
        linha = []
        for j in range(i+1):
            linha.append(i+1)
        print(*linha, sep=' ')

piramide(int(input('Digite o valor de n: ')))