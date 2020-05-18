from math import atan2, hypot

def get_angle(p1, p2):
    return atan2(p2[1]-p1[1], p2[0]-p1[0])

def get_distance(p1, p2):
    return hypot(p2[0]-p1[0], p2[1]-p1[1])

def coordinate_from_position(board, position):
    for square in board.squares:
        if square.position == position:
            return square.coordinate
