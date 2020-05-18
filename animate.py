import pygame
from math import sin, cos
from animate_helpers import get_angle, get_distance, coordinate_from_position
import main

# ----- not needed, added for testing
from random import randrange, shuffle
# !----------------------------------

SCREEN_SIZE = (900, 600)

animation_done = False


count_ = 0


# the input for this function is a list with positions,
# so positions[0] = (3, 4) -> means the first element
# in the list has to change position to (3, 4)
def animate_squares(board, positions, speed=30):
    angles = []
    coordinates = []
    count = 0
    animation_done = False
    # print("positions", positions)
    if not hasattr(board, "anim_coordinates"):
        board.anim_coordinates = []
        for pos in positions:
            board.anim_coordinates.append(coordinate_from_position(board, pos))
    coordinates = board.anim_coordinates
    if not hasattr(board, "anim_angles"):
        board.anim_angles = []
        for i, dest in enumerate(coordinates):
            if dest is None:
                dest = board.squares[i].coordinate
            board.anim_angles.append(
                get_angle(board.squares[i].coordinate, dest))
    angles = board.anim_angles

    # change all the positions of squares to that of which they should be
    for i, square in enumerate(board.squares):
        square.position = positions[i]

    # move the squares to the desired coordinates
    for i, square in enumerate(board.squares):
        if coordinates[i] == None:
            coordinates[i] = square.coordinate
        if get_distance(square.coordinate, coordinates[i]) > speed:
            square.coordinate = (
                square.coordinate[0] + cos(angles[i]) * speed, square.coordinate[1] + sin(angles[i]) * speed)
        else:
            square.reset_coordinate()
            count += 1
    if count == len(board.squares) - 1:
        animation_done = True


def rect_center(screen, fill, x, y, w, h, border=0):
    left_corner = (x - w / 2, y - h / 2)
    pygame.draw.rect(
        screen, fill, (left_corner[0], left_corner[1], w, h), border)


class Square:
    def __init__(self, board, position=(0, 0), color=(0, 0, 0)):
        self.board = board
        self.position = position
        self.reset_coordinate()
        self.color = color
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

    def reset_coordinate(self):
        self.coordinate = (self.board.coordinate[0] + self.position[0] * self.board.square_size[0] + self.board.square_size[0] / 2,
                           self.board.coordinate[1] + self.position[1] * self.board.square_size[1] + self.board.square_size[1] / 2)

    def display(self):
        rect_center(screen, (self.r, self.g, self.b),
                    self.coordinate[0], self.coordinate[1], self.board.square_size[0], self.board.square_size[1], 0)


class Board:
    def __init__(self, dimensions, size=SCREEN_SIZE, coordinate=(0, 0)):
        self.dimensions = dimensions
        self.coordinate = coordinate
        self.size = size
        self.square_size = (
            self.size[0] / self.dimensions[0], self.size[1] / self.dimensions[1])
        self.init_squares()

    def init_squares(self):
        self.squares = []
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                self.squares.append(Square(self, (i, j)))

    def display_squares(self):
        for i in self.squares:
            i.display()


board = Board((len(main.BOARD_HISTORY[0]), len(main.BOARD_HISTORY[0][0])))

# Define colors
BG_COLOR = pygame.Color("#F0F0F0")
MAIN_COLOR = pygame.Color("#0792D6")

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = SCREEN_SIZE
screen = pygame.display.set_mode(size)

pygame.display.set_caption("spread simulation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # GAME LOGIC

    # ----- not needed, added for testing
    if count_ < len(main.BOARD_HISTORY):
        for square in board.squares:
            BOARD = main.BOARD_HISTORY[count_]
            index = BOARD[square.position[0]][square.position[1]]
            if index == 0:  # asel e te "if not index:"
                square.b = square.r = 0
                square.g = 255
            elif index < 1:
                square.b = 0
                square.r = 255 * index
                square.g = 0
            elif index == 69:
                square.r = 0
                square.b = 190
                square.g = 0
            elif index == 1:
                square.r = 0
                square.b = 0
                square.g = 0
            shuffle = []
        if count_ < len(main.SHUFFLE_HISTORY):
            for i in main.SHUFFLE_HISTORY[count_]:
                shuffle.append(i)
            # animate_squares(board, shuffle)
            count_ += 1

    # -----------------------------------

    # Get Mouse Position
    #mousepos = pygame.mouse.get_pos()
    #mousex = mousepos[0]
    #mousey = mousepos[1]

    # DRAW
    screen.fill(BG_COLOR)
    board.display_squares()

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.time.wait(650)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
