from mars_rover.plateau import Plateau
from mars_rover.position import Position
from mars_rover.rover import Rover


def main():
    plateau = Plateau(5, 5)
    pos = Position(1, 2)
    rover = Rover(plateau, pos, Rover.PATH.get('N'))
    rover.process("LMLMLMLMM")
    print(rover)

    rover.set_pos(3, 3, Rover.PATH.get('E'))
    rover.process("MMRMMRMRRM")
    print(rover)


if __name__ == "__main__":
    main()
