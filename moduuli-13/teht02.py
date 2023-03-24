import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def haeLentoasema(code):
    sql = "SELECT name, municipality FROM airport WHERE ident = '" + (code) + "'"
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

@app.route("/kenttä/<code>")
def check(code):
    port = haeLentoasema(code)
    rep = {"ICAO": code, "Name":port[0][0], "Municipality":port[0][1]}
    return jsonify(rep)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)