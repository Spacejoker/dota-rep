import os
from flask import Flask, url_for, render_template, request, jsonify
from scrape import *
from model import *
from persist import *

app = Flask(__name__)
db = None

#ajax call to create html-content
@app.route('/_list_players')
def list_players():
    players = db.find_player()
    ret = '<ul>'
    for p in players:
        ret += '<li>name: '
        ret += p['name']
        ret += ', url: '
        ret += p['page_url']
        ret += '</li>'
    ret += '</ul>'
    return jsonify(player_list=ret)

#flask page with static content
@app.route('/heroes')
def heroes():
    hero = url_for('static', filename='alchemist.png')
     
    return render_template('heroes.html', hero=hero)

#scrape the web via ajax call
@app.route('/_game_search')
def game_search():
    players = gen_full_player_list()
    for p in players:
        db.save_player(p)

    data = '<span>Some text in a span</span>'
    return jsonify(gamelist=data)

@app.route('/')
def hello():
    return render_template('players.html')

if __name__ == '__main__':
    db = Database()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
