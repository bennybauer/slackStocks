from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/stock')
def stock():
    ticker = request.args.get('text')
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=l1"
    result = requests.get(url)
    return ticker.upper() + ": $" + str(result.json())

if __name__ == '__main__':
    app.debug = True
    app.run()
