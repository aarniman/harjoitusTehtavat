import math

sade = int(input("Anna ympyrän säde metreinä"))

vastaus = math.pi * sade ** 2
vastaus = round(vastaus, 2)

print(str(vastaus) + " m\u00b2")