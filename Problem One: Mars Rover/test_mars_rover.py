import unittest
from mars_rover.plateau import Plateau
from mars_rover.position import Position
from mars_rover.rover import Rover 


class TestPosition(unittest.TestCase):
    def testConstructor(self):
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

        position = Position(1, 2)
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 2)


class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 10)

        self.assertEqual(plateau.width, 7)
        self.assertEqual(plateau.height, 10)
 

class TestRover(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 7)
        position = Position(0, 0)

        rover = Rover(plateau, position, Rover.PATH['W'])

        self.assertEqual(Position(0, 0), rover.position)
        self.assertEqual(plateau, rover.plateau)


if __name__ == '__main__':
    unittest.main()
