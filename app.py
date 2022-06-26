from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    title = "Binance"
    return render_template('index.html', title=title)


@app.route("/buy/<int:myNum>")
def buy(myNum):
    print(myNum)
    return 'buy'

@app.route("/sell")
def sell():
    return 'sell'

@app.route("/history")
def history():
    con = sqlite3.connect('tdAmeritrade.db')
    cur = con.cursor()
    # limite de resultados via queryString
    select_stmt = 'select seq, timestamp, high_price, open_price, close_price, low_price, volume from CHART_FUTURES order by seq desc limit 10'

    data =[]

    for row in cur.execute(select_stmt):
        row = {'time': row[1], 'high' : row[2], 'open' : row[3], 'close' : row[4], 'low' : row[5]}
        data.append(row)

    con.close()

    return json.dumps(data)