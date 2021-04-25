class Person():
    def __init__(self):
        self.name = ''

        self.blood = 100
        self.attack = 50
        self.defence = 20
        self.exp = 0
        self.maxexp = 10000
        self.gold = 0

    def set_name(self, name):
        self.name = name