from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/stock')
def stock():
    ticker = request.args.get('text')
    # Get price, amount change, percent change, day high, day low
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=l1c1p2hg"
    result = requests.get(url).text.split(',')
    result[2] = result[2].replace('"','')
    result[4] = result[4].replace('\n','')
    result_text = ("*" + ticker.upper() + "*" + "\n"
                    "Price: " + result[0] + "\n"
                    "Amt Change: " + result[1] + "\n"
                    "% Change: " + result[2] + "\n"
                    "Day High: " + result[3] + "\n"
                    "Day Low: " + result[4])
    return result_text

if __name__ == '__main__':
    app.debug = True
    app.run()
