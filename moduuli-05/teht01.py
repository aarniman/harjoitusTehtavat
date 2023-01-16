import random

maara = int(input("Montako noppaa heitetään?"))
yht = 0
luku = 0
for i in range(maara):
    yht = yht + random.randint(1,6)
print(yht)