function Match(hero, match_id, k, d, a){
    var self = this;
    self.hero = hero;
    self.match_id = match_id;
    self.k = k;
    self.d = d;
    self.a = a;
}

function Hero(name){
    var self = this;
    self.name = name;
}

var myModel = {
    self : this,
    status : ko.observable('Status'),
    row_data : ko.observableArray([]), 
    matches :  ko.observableArray([]),
    heroes : ko.observableArray([]),
    addRow : function(data) {
        this.matches.push(new Match(data.player, data.match_id, data.k, data.d, data.a));
    },
    addHero : function(data) {
        this.heroes.push(new Hero(data));
    }
};

$(function(){
    ko.applyBindings(myModel);
    var all_heroes = ["Pugna", "Windrunner"];
    $.getJSON($SCRIPT_ROOT + '/_load_heroes', {
    }, function(data) {
        var heroes = data.data;

        for(var i = 0; i < heroes.length; i ++){
            self.myModel.addHero(heroes[i].name);
        }
    });
});

$(function() {
    $('button#load_games').bind('click', function() {
        $.getJSON($SCRIPT_ROOT + '/_load_games', {
            hero_name: $('input[id=search]').val()
        }, function(data) {
            var d = data.matches;
            self.myModel.matches([]);
            for(var i = 0; i < d.length; i++){
                self.myModel.addRow(d[i]);
            }
            self.myModel.status('UPDATE');
        });
        return false;
    });
});

