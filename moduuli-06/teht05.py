
def parittomatPois(lista):
    lista2 = []
    for i in range(len(lista)):
        if(lista[i] % 2 != 0):
            continue
        else:
            lista2.append(lista[i])
    return lista2

l = [1,2,3,4,5,6,7,8,9,10]
print(parittomatPois(l))
print(l)