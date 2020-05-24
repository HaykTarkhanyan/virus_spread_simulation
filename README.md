This is a toy simulation of how a virus spreads.

**Note**: There isn't argparser now, so you'll need to change parameters directly from the file

GREEN - not infected  
BLUE - recovered  
BlACK - dead
<p float="left">
<img src="https://github.com/HaykTarkhanyan/virus_spread_simulation/blob/master/moviee.gif" alt = "spread_gif" width="49%" height = "49%" >
<img src="https://github.com/HaykTarkhanyan/virus_spread_simulation/blob/master/demo_2.gif" alt = "spread_gif" width="49%" height = "49%" >
</p>

We have following parameters to play with:

**BOARD_HEIGHT** (default: 50)  
**BOARD_WIDTH** (default: 50)   

**INFECTION_CHANCE** (default: 0.8)
*Chance of being infected from a neighbor*
**INFECTING_OPTION** (default: "line")
*Defines the common element of two neighbors; either “line” or “point”*
**INITIAL_INFECTED** (default: 2)

**SEVERNES**  (default: 0.3)
*How hard it is to cure patients*
**RECOVERY_RATE** (default: 0.3)
**SEVERNESS_DECAY** (default: 0.95)
*Rate by which VIRUS_SEVERNES drops after we begin recovering*

**START_DEEPENING** (default: 4)   -  after N th day the health will slowly get worse       
**START_EMERGENCY** (default: 8)  -  we drop the transportation and number of people treveling              
**START_RECOVERING** (default: 9) -  People start to recover                  

**PLOT_RESULTS** - weather to save the results
Currently, we save the gif by default

###not globals but parameters to run_simulation

**shuffle_every** (def: 1), - Every n day people change their location
**shuffle_qunatity** (def :BOARD_HEIGHT * BOARD_WIDTH // 10) how many people to shuffle

**transportation_drop** (def : 3) - After emergancy was declared how many times
                                to decrease shuffle_quantitu
**infection_drop**( def: 2) - like transportation drop but with virus severness


