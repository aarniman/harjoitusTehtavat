pituus = int(input("Kerro kuhan pituus senttimetreinä \n"))

if(pituus < 37):
    ero = 37-pituus
    print("Kuha on alimittainen joten laske se takaisin järveen. Kuha on " + str(ero) + " senttiä liian lyhyt.")
else:
    print("Nyt on komea saalis!")