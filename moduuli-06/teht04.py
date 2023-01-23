
def summa(lista):
    yht = 0
    for i in range(len(lista)):
        yht = yht + lista[i]
    return yht

l = [19,42,53,24,7,57,9, -43]
print(str(summa(l)))