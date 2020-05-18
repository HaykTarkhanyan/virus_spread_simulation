This is a toy simulation of how a virus spreads.
Note: Since writing argparser is boring, you will need to open main.py, change globals and enjoy the simulation.
We start with a given size of board and number of infected people (default: 1)

We have following parameters to play with
BOARD_HEIGHT (default: 50)
BOARD_WIDTH (default: 50)
INFECTION_CHANCE (default: 0.8)
Chance of being infected from a neighbor
INFECTING_OPTION (default: "line")
Defines the common element of two neighbors; either “line” or “point”
INITIAL_INFECTED (default: 2)
VIRUS_SEVERNES  (default: 0.3)
How hard it is to cure patients
RECOVERY_RATE (default: 0.3)
SEVERNESS_DECAY (default: 0.95)
Rate by which VIRUS_SEVERNES drops after we begin recovering
START_DEEPENING = 5         -  after Nth day the health will slowly vatanam
START_EMERGENCY = 10     -  we drop the transportation and number of people treveling
START_RECOVERING = 15    -
PLOT_RESULTS
shuffle_every=1,
                   shuffle_qunatity=BOARD_HEIGHT * BOARD_WIDTH // 10,
                   transportation_drop=3, infection_drop=2




Every morning the following happens:
All infecteds peoples health codtination vatanuma
All alive infecteds try to infect their neigbors
Depending on which day it is ingectets health lavanuma
virus severness drops aaaaaaaaaaaaaa, Apr lav chi etum sec



