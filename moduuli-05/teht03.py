luku = int(input("Anna luku"))
flag = False
if luku == 1:
    print("Luku ei ole alkuluku")
else:
    for i in range(2,luku):
        if(luku % i == 0 and i > 1 and i < luku):
            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")
