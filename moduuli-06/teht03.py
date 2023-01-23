
def bensaMuunnin(gallona):
    litraa = gallona * 3.785
    return litraa

while True:
    luku = int(input("Anna galloni jotka haluat muuttaa. Negatiivinen lopettaa."))
    if luku < 0:
        break
    litra = bensaMuunnin(luku)
    print(f"{luku} gallonia bensaa on {litra} litraa bensaa.")