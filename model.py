
class Player():
    def __init__(self, name=None, page_url=None):
        self.name = name
        self.page_url = page_url
        self.top_heroes = None

    def __str__(self):
        return "name: " + self.name + ", url: " + self.page_url

class PlayerDetails():
    def __init__(self, top_heroes=[]):
        self.top_heroes = top_heroes

class Hero():
    def __init__(self, name, img_link):
        self.name = name
        self.img_link = img_link

    def __str__(self):
        print self.img_link
        return "Hero name: " + self.name + "."
