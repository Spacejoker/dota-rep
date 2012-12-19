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
    return 'Hello admin'

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

#List games per search criteria (hero_name)
@app.route('/_load_games')
def load_games():
    print 'server'
    hero_name = request.args.get('hero_name')
    matches = db.find_match(hero_name)
    print 'a'
    #process result before showing
    for m in matches:
        m['summary'] = 'The summary'
        for h in m['heroes']:
            if h['hero'] == hero_name:
                m['summary'] = str(hero_name) + ' played by ' + str(h['player'])
    ret = {'matches' : matches}
    print 'b'
    return jsonify(**ret)

#clear heroes
@app.route('/_remove_hero')
def remove_hero():
    db.remove_hero() 
    return jsonify(result='All heroes deleted')

#scrape heroes
@app.route('/_refresh_heroes')
def refresh_heroes():
    #request.args.get('heroname')
    heroes = scrape.refresh_heroes(db)
    return jsonify(result='Success, nr of new heroes: ' + str(len(heroes)))


#flask page with static content
@app.route('/heroes')
def heroes():
    hero_list = db.find_hero()
    ret = ""
    for h in hero_list:
        ret += '<img src="' + url_for('static', filename='hero_img/' + h.img_link) + '"/>'
    print ret
    hero = Markup(ret)
    return render_template('heroes.html', hero=hero)

if __name__ == '__main__':
    db = Database()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
