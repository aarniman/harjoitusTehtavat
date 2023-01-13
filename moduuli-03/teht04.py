vuosi = int(input("Anna vuosiluku"))

if(vuosi % 4 == 0):
    print("Vuosi on karakusvuosi")
elif(vuosi % 100 == 0):
    if(vuosi % 400 == 0):
        print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")