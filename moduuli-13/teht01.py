from flask import Flask, jsonify

app = Flask(__name__)

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

@app.route("/alkuluku/<int:num>")
def check(num):
    rep = {"Numero": num, "isPrime": isPrime(num)}
    return jsonify(rep)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)