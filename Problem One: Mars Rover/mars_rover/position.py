class Position:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, pos):
        return self.x == pos.x and self.y == pos.y