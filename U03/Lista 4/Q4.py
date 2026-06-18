N = int(input('Digite um valor: '))

def getInverso(n:int):
    n = str(n)
    res=''
    for i in range(len(n), 0, -1):
        res += n[i-1]
    return res

print(getInverso(N))