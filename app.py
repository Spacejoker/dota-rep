import os
from flask import Flask, url_for, render_template, request, jsonify
import urllib2

app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_game_search')
def game_search():
    raw_html = urllib2.urlopen('https://dotabuff.com/players/verified').read()

    print raw_html
    print "html above"
    data = '<span>Some text in a span</span>'
    return jsonify(gamelist=data)

@app.route('/')
def hello():
    return render_template('tmp.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
