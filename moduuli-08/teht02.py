import mysql.connector

def haeLentoasemienMaara(code):
    maara = 0
    sql = "SELECT type FROM airport WHERE iso_country = '" + (code) + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    calc = {i: result.count(i) for i in result}
    print(calc)
    return


connection = mysql.connector.connect(host='localhost',
                                     port= 3306,
                                     database='flight_game',
                                     user='Arnie',
                                     password='testi',
                                     autocommit=True
                                     )

while True:
    search = input("Anna maakoodi. Tyhjä lopetaa")
    if(search == ""):
        break
    haeLentoasemienMaara(search)