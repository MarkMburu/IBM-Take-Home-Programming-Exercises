import pytest
from mars_rover.plateau import Plateau
from mars_rover.position import Position
from mars_rover.rover import Rover

def test_position():
    position = Position(0, 0)
    assert position.x == 0
    assert position.y == 0
    position = Position(1, 2)
    assert position.x == 1
    assert position.y == 2

def test_plateau():
    plateau = Plateau(7, 10)
    assert plateau.width == 7
    assert plateau.height == 10

def test_rover():
    plateau = Plateau(7, 7)
    position = Position(0, 0)
    rover = Rover(plateau, position, Rover.PATH['W'])
    assert Position(0, 0) == rover.pos
    assert plateau == rover.plateau
