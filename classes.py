class Table:

    n_sides = 4

    def __init__(self, n_legs):
        self.n_legs = n_legs
        self.n_chairs = 4

    def set_chairs(self, n_chairs):
        self.n_chairs = n_chairs


def main():
    table = Table(4)
    table.set_chairs(100)
    print(table.n_legs)

main()

