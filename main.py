"""
Written by Hayk Aprikyan and Hayk Tarkhanyan

Date finished - 11.04.2020
"""

import random
import numpy as np
from plot_utils import plot_data


BOARD_HEIGHT = 100
BOARD_WIDTH = 100

INFECTION_CHANCE = 1
INFECTING_OPTION = "line"
INITIAL_INFECTED = 1
VIRUS_SEVERNES = 0.3

RECOVERY_RATE = 0.3
SEVERNESS_DECAY = 0.95

START_DEEPENING = 1
START_EMERGENCY = 7
START_RECOVERING = 10

INFECTED = []
RECOVERED = []
DEAD = []
ALL_ALIVE = [[i, j] for i in range(BOARD_HEIGHT) for j in range(BOARD_WIDTH)]

vir_sev = VIRUS_SEVERNES
inf_chance = INFECTION_CHANCE

PLOT_RESULTS = True


def initialize_board(width, height):
    """
    Returns 2-D array with shape (width,
    height), filled with 0's representing
    the population.
    """
    return np.zeros((width, height))


BOARD = initialize_board(BOARD_HEIGHT, BOARD_WIDTH)


def infect(person, dose_min=VIRUS_SEVERNES, dose_dev=VIRUS_SEVERNES / 2):
    """
    Increases a healthy person's level of
    infection with some initial random dose.

    ARGS :
    person - list, tuple, or array,  indicates persons location on the board
    dose_min - float or int, is the mu paramtrs of gaussian distrib.
               default calue - VIRUS_SEVERNESS
    dose_dev - float or int, is the sigma paramtrs of gaussian distrib.
               default calue - VIRUS_SEVERNESS / 2
    """
    global VIRUS_SEVERNES

    # we make the assumption that person can be infected only once
    if [person[0], person[1]] not in RECOVERED:
        BOARD[person[0], person[1]
              ] += abs(np.random.normal(dose_min, dose_dev))
        if 1 > BOARD[person[0], person[1]] > 0:
            INFECTED.append([person[0], person[1]])


def start_pandemic(num_to_infect=1):
    """
    Start pandemic by infecting randomly
    selected people of given number.

    Args:
    num_to_enfect - int, default value  - 1
    """
    for i in range(num_to_infect):
        rand_y = np.random.randint(0, BOARD_WIDTH)
        rand_x = np.random.randint(0, BOARD_HEIGHT)
        while BOARD[rand_x, rand_y]:
            rand_y = np.random.randint(0, BOARD_WIDTH)
            rand_x = np.random.randint(0, BOARD_HEIGHT)
        else:
            infect((rand_x, rand_y))


def die(person):
    """
    Kills a person with value 1 or greater,

    ARGS:
    person - list, tuple, or array,  indicates persons location on the board
    """
    DEAD.append(person)
    INFECTED.remove(person)
    if person in ALL_ALIVE:
        ALL_ALIVE.remove(person)
    else:
        raise Warning(f"Person {person} wasn't found in ALL_ALIVE")


def fully_recover(person):
    """
    Heals a person with value 0 or less,
    given his location, tuple, list or array.

    ARGS:
    person - list, tuple, or array,  indicates persons location on the board
    """
    RECOVERED.append(person)
    INFECTED.remove(person)


def shuffle(people):
    """
    Function takes array of people and changes
    their places with places of randomly
    selected people (as well changes their states(recovered, dead, health))

    """
    alive = ALL_ALIVE.copy()

    for i in people:
        alive.remove(i)

    all_new_locations = random.sample(alive, len(people))

    # never write code like this, if you had let's say 5 more
    # lists would you write 24 ifs?
    for i, j in zip(people, all_new_locations):
        # changes the status
        if i in INFECTED and j in INFECTED:
            pass

        elif i in RECOVERED and j in RECOVERED:
            pass

        elif i in INFECTED and j in RECOVERED:
            INFECTED.remove(i)
            INFECTED.append(j)
            RECOVERED.remove(j)
            RECOVERED.append(i)

        elif i in RECOVERED and j in INFECTED:
            RECOVERED.remove(i)
            RECOVERED.append(j)
            INFECTED.remove(j)
            INFECTED.append(i)

        elif i in RECOVERED and j not in INFECTED:
            RECOVERED.remove(i)
            RECOVERED.append(j)

        elif i in INFECTED and j not in RECOVERED:
            INFECTED.remove(i)
            INFECTED.append(j)

        elif i not in RECOVERED and j in INFECTED:
            INFECTED.remove(j)
            INFECTED.append(i)

        elif i not in INFECTED and j in RECOVERED:
            RECOVERED.remove(j)
            RECOVERED.append(i)

    for old, new in zip(people, all_new_locations):
        # changes the values
        placeholder = BOARD[new[0], new[1]]
        BOARD[new[0], new[1]] = BOARD[old[0], old[1]]
        BOARD[old[0], old[1]] = placeholder


def infect_neighbors(person, option=INFECTING_OPTION):
    '''
    Infects person's neighbors given the argument.

    Arguments:

    person - list, tuple, or array,  indicates persons location on the board
    Option (default=INFECTING_OPTION): defines the common
    element of two neighbors. Values: ["line", "point"].
    '''
    # make understandable this
    if option == "point":
        neighbors = np.array([(i, j)
                              for i in range(person[0] - 1, person[0] + 2)
                              for j in range(person[1] - 1, person[1] + 2)
                              if 0 <= i < BOARD_HEIGHT and 0 <= j < BOARD_WIDTH
                              and (i, j) != (person[0], person[1])
                              and not BOARD[i, j]])

    elif option == "line":
        neighbors = np.array([(i, j) for i, j in zip([person[0], person[0],
                                                      person[0] - 1, person[0] + 1],
                                                     [person[1] - 1, person[1] + 1,
                                                      person[1], person[1]])
                              if 0 <= i < BOARD_HEIGHT and 0 <= j < BOARD_WIDTH
                              and BOARD[i, j] == 0])

    else:
        # add 3rd option where you infect by line with inf_chance, and those
        # who share point but not line with inf_chance//2
        raise Exception("Wrond type, choose either 'line' or 'point'")

    multiple_infect(neighbors)


def multiple_infect(neighbors, chance=INFECTION_CHANCE):
    """
    Function takes array of coordinates,
    and for each infects or not randomly.

    Args:
    chance - int, default - INFECTION_CHANCE
    """
    num_of_people = neighbors.shape[0]
    possibs = np.random.random([num_of_people, 1])

    for i in range(num_of_people):
        if possibs[i] < chance:
            infect(neighbors[i])


def spread_pandemic(infecteds):
    """
    Given a list of infecteds, infects their neighbors.
    """
    infecteds_copy = infecteds.copy()
    infecteds = []
    for i in infecteds_copy:
        infect_neighbors(i, INFECTING_OPTION)


def deepen_disease(person, mu=VIRUS_SEVERNES, sigma=VIRUS_SEVERNES / 2):
    """
    Increments person's disease with normal
    distribution, with given mu and sigma.
    """
    BOARD[person[0], person[1]] = min(
        BOARD[person[0], person[1]] + abs(np.random.normal(mu, sigma)), 1)

    if BOARD[person[0], person[1]] == 1:
        die(person)


def multiple_deepen(infecteds, mu=VIRUS_SEVERNES, sigma=VIRUS_SEVERNES / 2):
    """
    Deepens everyone's disease, calling
    deepen_disease() with given mu and
    sigma on everyone in infecteds.
    """
    for infected in infecteds:
        deepen_disease(infected, mu, sigma)


def recover(person, mu=RECOVERY_RATE, sigma=RECOVERY_RATE / 2):
    """
    Decreases person's disease with normal
    distribution, with given mu and sigma.
    """
    BOARD[person[0], person[1]] = max(BOARD[person[0], person[1]] -
                                      abs(np.random.normal(mu, sigma)), 0)


def multiple_recover(infecteds, mu=RECOVERY_RATE, sigma=RECOVERY_RATE / 2):
    """
    Tries to recover everyone's disease from
    given array, calling recover() with given mu and
    sigma on everyone in infecteds.

    Args:

    Infecteds -np.array, or list of tuples
    coefficent, sigma - integers(for gaussina distrib.)

    """
    for infected in infecteds[:]:
        recover(infected, mu, sigma)
        if BOARD[infected[0], infected[1]] == 0:
            fully_recover(infected)


def run_simulation(shuffle_every=1,
                   shuffle_qunatity=BOARD_HEIGHT * BOARD_WIDTH // 100,
                   transportation_drop=3, infection_drop=2, output=True):
    """
    gathes all the helper function in one place and runs one single iteration of pandemic

    """

    global BOARD, INFECTED, DEAD, RECOVERED, ALL_ALIVE, VIRUS_SEVERNES, \
        SEVERNESS_DECAY, RECOVERY_RATE, INFECTION_CHANCE

    num_all_people = BOARD_HEIGHT * BOARD_WIDTH
    # stuff needed for visualizations
    inf = []
    rec = []
    dead = []

    if output:
        print("Starting the simulation, parameters are: ")
        print(f"Board size - {BOARD_HEIGHT}x{BOARD_WIDTH}")
        print("-" * 35)
        print(f'Emergancy start - {START_EMERGENCY}')
        print(f'Deepening start - {START_DEEPENING}')
        print(f'Recovering start - {START_RECOVERING}')
        print("-" * 35)
        print(f'Virus severness - {VIRUS_SEVERNES}')
        print(f'Virus severness decay - {SEVERNESS_DECAY}')
        print("-" * 35)
        print(f'Infection chance - {INFECTION_CHANCE}')
        print(f'Initial infecteds - {INITIAL_INFECTED}')
        print(f'Infecting method - {INFECTING_OPTION}')
        print("-" * 35)

        print("Starting the pandemic")
        print("Day 1\n")
        print("Num infected: 1")

    start_pandemic()
    BOARD = BOARD.round(2)
    if output:
        print(BOARD)

    i = 2  # i is short for day number :D

    while True:
        # starting emergency:
        if i == START_EMERGENCY:
            shuffle_qunatity //= transportation_drop

            INFECTION_CHANCE //= infection_drop

        if i % shuffle_every == 0:

            if len(ALL_ALIVE) >= shuffle_qunatity * 2:
                people_to_shuffle = random.sample(ALL_ALIVE, shuffle_qunatity)

                shuffle(people_to_shuffle)

        if i >= START_DEEPENING:
            multiple_deepen(INFECTED)

        if i >= START_RECOVERING:
            multiple_recover(INFECTED)
            # decreas severness so that more people will recover
            VIRUS_SEVERNES *= SEVERNESS_DECAY ** (i - START_RECOVERING)

        spread_pandemic(INFECTED)

        inf.append(len(INFECTED))
        dead.append(len(DEAD))
        rec.append(len(RECOVERED))

        BOARD = BOARD.round(2)

        if output:
            print("Day {}".format(i))
            print(BOARD)
            print("Num infected: {}".format(len(INFECTED)))
            print("Num dead: {}".format(len(DEAD)))
            print("Num recovered: {}".format(len(RECOVERED)))

        # es arji hanel
        if len(DEAD) + len(INFECTED) + len(RECOVERED) > BOARD_HEIGHT * BOARD_WIDTH:
            raise Exception("Turns out we left a big!!!!")

        if len(DEAD) == num_all_people:
            if output:
                print(f"All died in {i} days")

            return [inf, dead, rec]

        if len(RECOVERED) == num_all_people or \
           len(INFECTED) == 0:

            if output:
                print(f"All revovered. Took {i} days")

            return [inf, dead, rec]

        if output:
            print("-" * 35)

        i += 1


if __name__ == "__main__":
    inf, dead, rec = run_simulation(3, output=True)

    if PLOT_RESULTS:
        print("plotting data")
        plot_data(inf, dead, rec, START_EMERGENCY, START_DEEPENING,
                  START_RECOVERING, vir_sev, inf_chance)
        print("Saved plots")