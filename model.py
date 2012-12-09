class Player():
    def __init__(self, name=None, page_url=None):
        self.name = name
        self.page_url = page_url

    def __str__(self):
        return "name: " + self.name + ", url: " + self.page_url

