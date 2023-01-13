sp = input("Kerro biologinen sukupuolesi")

if(sp == "mies"):
    hg = int(input("Anna hemoglobiinisi arvo"))
    if(hg < 134):
        print("Hemoglobiininne on liian alhainen hyvä herra.")
    elif(hg > 195):
        print("Hemoglobiininne on liian korkea hyvä herra.")
    else:
        print("Hemoglobiininne on juuri sopiva hyvä herra.")
elif(sp == "nainen"):
    hg = int(input("Anna hemoglobiinisi arvo"))
    if(hg < 117):
        print("Hemoglobiininne on liian alhainen hyvä neiti.")
    elif(hg > 175):
        print("Hemoglobiininne on liian korkea hyvä neiti.")
    else:
        print("Hemoglobiininne on liian alhainen hyvä neiti.")
else:
    print("Virheellinen sukupuoli")