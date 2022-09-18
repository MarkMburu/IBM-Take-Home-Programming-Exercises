from mars_rover.position import Position


class Rover:
    GRID_POINTS = {
        'M': 'forward',
        'L': 'left',
        'R': 'right',
    }

    PATH = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    start = PATH['N']

    def __init__(self, plateau, pos, start):
        self.plateau = plateau
        self.pos = pos
        self.start = start

    def __str__(self):
        return self.current_pos

    def set_pos(self, x, y, start):
        if not isinstance(self.pos, Position):
            self.pos = Position(x, y)
        else:
            self.pos.x = x
            self.pos.y = y
        self.start = start

    @property
    def current_pos(self):
        return '{} {} {}'.format(self.pos.x, self.pos.y, self.get_start)

    @property
    def get_start(self):
        PATH = list(self.PATH.keys())
        try:
            path = PATH[self.start - 1]
        except IndexError:
            path = 'N'
        return path

    def process(self, grids):
        for i in range(len(grids)):
            self.run_grid(grids[i])

    def run_grid(self, grid):
        if 'L' == grid:
            self.left()
        elif 'R' == grid:
            self.right()
        elif 'M' == grid:
            if not self.forward():
                pass
        else:
            print("Invalid input!")

    def forward(self):
        if not self.plateau.available_moves(self.pos):
            return False
        if self.PATH['N'] == self.start:
            self.pos.y += 1
        elif self.PATH['E'] == self.start:
            self.pos.x += 1
        elif self.PATH['S'] == self.start:
            self.pos.y -= 1
        elif self.PATH['W'] == self.start:
            self.pos.x -= 1
        return True

    def left(self):
        self.start = self.PATH['W'] if (
            self.start - 1) < self.PATH['N'] else self.start - 1

    def right(self):
        self.start = self.PATH['N'] if (
            self.start + 1) > self.PATH['W'] else self.start + 1
