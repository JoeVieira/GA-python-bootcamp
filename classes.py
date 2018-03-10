class Table:

    n_sides = 4

    def __init__(self, n_legs):
        self.n_legs = n_legs
        self.n_chairs = 4

    def set_chairs(self, n_chairs):
        self.n_chairs = n_chairs



class BaseballPlayer:

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def lookUpStats(self):
        if self.name == "david":
            return 1000
        elif self.name == "billy":
            return 10


class CricketPlayer:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def lookUpStats():
        if name == "david":
            return 1000
        elif name == "billy":
            return 10



def main():
    david = CricketPlayer("david","redsox")
    david2 = CricketPlayer("david", "redsox")
    things = dir(david)
    billy = BaseballPlayer("billy", "rangers")


main()
