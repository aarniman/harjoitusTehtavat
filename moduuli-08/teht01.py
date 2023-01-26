import mysql.connector

def haeLentoasema(code):
    sql = "SELECT name FROM airport WHERE ident = '" + (code) + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for rivi in result:
            print(rivi)
    return


connection = mysql.connector.connect(host='localhost',
                                     port= 3306,
                                     database='flight_game',
                                     user='Arnie',
                                     password='testi',
                                     autocommit=True
                                     )

while True:
    search = input("Anna ICAO-koodi. Tyhjä lopetaa")
    if(search == ""):
        break
    haeLentoasema(search)