number = int(input("Anna kuukauden numero"))

seasons = ("kevät", "kesä", "syksy", "talvi")
if number == 12 or number == 1 or number == 2:
    season = seasons[3]
    print(f"{number}. kuukausi on osa {season}-vuodenaikaa")
elif number == 3 or number == 4 or number == 5:
    season = seasons[0]
    print(f"{number}. kuukausi on osa {season}-vuodenaikaa")
elif number == 6 or number == 7 or number == 8:
    season = seasons[1]
    print(f"{number}. kuukausi on osa {season}-vuodenaikaa")
elif number == 9 or number == 10 or number == 11:
    season = seasons[2]
    print(f"{number}. kuukausi on osa {season}-vuodenaikaa")
else:
    print("Annoit väärän vuodenajan")
