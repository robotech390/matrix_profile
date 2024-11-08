lista = [1,11,11,11,11,11,11,11,11,111,11,11,1,1,1,1,1,11,1,1]
n = 4

def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]

listaCortada = list(divide_chunks(lista, n))
print(listaCortada)
