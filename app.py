import os
from flask import Flask, url_for, render_template, request, jsonify, Markup
from scrape import *
import scrape
from model import *
from persist import *

app = Flask(__name__)
db = None

#http://24ways.org/2012/how-to-make-your-site-look-half-decent/
#http://twitter.github.com/bootstrap/

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

@app.route('/abc')
def abc():
    print 'hello' 
    return render_template('k.html', hero_list = [])

#Admin site
@app.route('/admin')
def admin():
    heroes = db.find_hero()
    ret = '<ul>'
    for h in heroes:
        ret += '<li>' + str(h) + '</li>'
    ret += '</ul>'
    return render_template('admin.html', hero_list = ret)

@app.route('/_load_games')
def load_games():
    hero_name = request.args.get('hero_name')
    print hero_name
    matches = db.find_match(hero_name)
    print len(matches)
    #games = scrape.get_latest_games(player_id)
    
    #process result before showing
    for m in matches:
        print m
        m['summary'] = 'The summary'
        for h in m['heroes']:
            print h
            if h['hero'] == hero_name:
                print 'match!'
                m['summary'] = str(hero_name) + ' played by ' + str(h['player'])
    print 'after'
    ret = {'matches' : matches}
    print 'RET:'
    print ret
    #ret = {'matches': [{'heroes': [{'player': 'DotAholi...', 'hero': 'Weaver'}], '_id': ObjectId('50d1079e9eae4f5309164f1c'), 'type': 'match', 'match_id': u'Match 79804452'}]}
    print 'returning from server'
    return jsonify(**ret)

@app.route('/_remove_hero')
def remove_hero():
    db.remove_hero() 
    return jsonify(result='All heroes deleted')

@app.route('/_refresh_heroes')
def refresh_heroes():
    #request.args.get('heroname')
    heroes = scrape.refresh_heroes(db)
    return jsonify(result='Success, nr of new heroes: ' + str(len(heroes)))

@app.route('/matches_list')
def hero_list():
    return render_template('matches_list.html', hero_list="abc")

#flask page with static content
@app.route('/heroes')
def heroes():
    print 'routing ok'
    hero_list = db.find_hero()
    print 'dbcall ok'
    ret = ""
    for h in hero_list:
        ret += '<img src="' + url_for('static', filename='hero_img/' + h.img_link) + '"/>'
    print ret
    hero = Markup(ret)
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
