class Plateau:

    def __init__(self, width, height, min_width=0, min_height=0):
        self.width = width
        self.height = height
        self.MIN_WIDTH = min_width
        self.MIN_HEIGHT = min_height

    def available_moves(self, pos):
        return self.MIN_WIDTH <= pos.x <= self.width and self.MIN_HEIGHT <= pos.y <= self.height
