import geopy
import mysql.connector
from geopy import distance

def haeLentoasemat(code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + (code) + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


connection = mysql.connector.connect(host='localhost',
                                     port= 3306,
                                     database='flight_game',
                                     user='Arnie',
                                     password='testi',
                                     autocommit=True
                                     )

while True:
    search = input("Anna ICAO-koodi. Tyhjä lopetaa.\n")
    if(search == ""):
        break
    search2 = input("Anna toinen ICAO-koodi.\n")

    loc1 = haeLentoasemat(search)
    loc2 = haeLentoasemat(search2)
    diff = distance.distance(loc1, loc2).km
    diff = round(diff, 2)
    print(f"Lentokentät ovat {diff} kilometrin päässä toisistaan.")