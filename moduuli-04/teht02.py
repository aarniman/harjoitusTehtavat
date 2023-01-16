while True:
    tuuma = int(input("Anna tuuma. Loputa antamalla negatiivinen luku"))
    if(tuuma < 0):
        break
    sentti = tuuma * 2.54
    if tuuma > 1 or tuuma == 0:
        print(f"{tuuma} senttimetriä on {sentti} tuumaa")
    elif tuuma == 1:
        print(f"{tuuma} senttimetri on {sentti} tuumaa")
