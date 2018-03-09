class Table:

    n_chairs = 4
    n_sides = 4
    n_legs = 0

    def __init__(self, n_legs):
        self.n_legs = n_legs

    def set_chairs(self, n_chairs):
        self.n_chairs = n_chairs


def main():
    table = Table(4)
    table.set_chairs(100)
    print(table.n_legs)

main()

