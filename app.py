import os
from flask import Flask, url_for, render_template, request, jsonify, Markup
from scrape import *
import scrape
from model import *
from persist import *

app = Flask(__name__)
db = None

#http://24ways.org/2012/how-to-make-your-site-look-half-decent/

#Admin site, implement correctly
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/matches_list')
def hero_list():
    return render_template('matches_list.html')

#ajax section:
#Scrape a game by ID, for admin/debug
@app.route('/_scrape_game')
def scrape_game():
    print 'ok'
    match_id = int(request.args.get('match_id'))
    print 'ok2'
    for m_id in range(match_id, match_id + 20):
        print 'scraping game' + str(m_id)
        try: 
            add_match(str(m_id), db)
        except: 
            print 'problem with game ' + str(m_id)

    return jsonify()

@app.route('/admin/_scrape_player')
def scrape_player():
    player_id = request.args.get('match_id')
    scrape.scrape_player(player_id, db)
    ret = {}
    return jsonify(**ret)

@app.route('/admin/_status')
def status():
    players = db.find_player()
    match_cnt = db.count_matches()
    ret = {'games_played' : str(match_cnt), 'players' : players}
    return jsonify(**ret)

#List games per search criteria (hero_name)
@app.route('/_load_games')
def load_games():
    hero_name = request.args.get('hero_name')
    matches = db.find_match(hero_name)
    
#process result before showing
    for m in matches:
        m['summary'] = 'The summary'
        for h in m['heroes']:
            if h['hero'] == hero_name:
                m['summary'] = hero_name + ' played by ' + h['player']
                m['player'] = h['player']
                m['k'] = h['k']
                m['d'] = h['d']
                m['a'] = h['a']
    ret = {'matches' : matches}
    return jsonify(**ret)

@app.route('/_load_heroes')
def load_heroes():
    heroes = db.find_hero()
    ret = { 'data' : heroes }
    return jsonify(**ret)

#clear matches
@app.route('/admin/_remove_match')
def remove_match():
    db.remove_match()
    return jsonify(result='success')

#clear heroes
@app.route('/_remove_hero')
def remove_hero():
    db.remove_hero() 
    return jsonify(result='All heroes deleted')

#scrape heroes
@app.route('/_refresh_heroes')
def refresh_heroes():
    heroes = scrape.refresh_heroes(db)
    return jsonify(result='Success, nr of new heroes: ' + str(len(heroes)))

if __name__ == '__main__':
    db = Database()
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
