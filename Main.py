import random
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

universe_size = (100,100)

seeds = {  
    "beacon":[
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ],
    "sun":[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}

functions = { "pureSurvival", "diseaseSurvival", "wideSurvival", "spontLife", "spontDeath"

}

def setup():

    choice = " "
    seed_choice = " "
    
    while choice not in functions:
        print("What ruleset would you like to use?")
        choice = input()

    while seed_choice not in seeds:
        print("What seed would you like to use?")
        seed_choice = input()

        
    return choice, seed_choice 






def generation(universe, surv_choice, index_universe):
    
    new_universe = np.copy(universe)

    # Simple loop over every possible xy coordinate.
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            if surv_choice == "spontLife":
                new_universe[i,j] = eval(surv_choice + "(i, j, universe, index_universe)")
            elif surv_choice == "spontDeath":
                new_universe[i,j] = eval(surv_choice + "(i, j, universe, index_universe)")
            else:
                new_universe[i,j] = eval(surv_choice + "(i, j, universe)")

    # Set universe to be equal to new_universe.
    universe = np.copy(new_universe)
    return universe

def diseaseSurvival(x, y, universe):
    """
    Compute one iteration of Life for one cell.
    :param x: x coordinate of cell in the universe
    :type x: int
    :param y: y coordinate of cell in the universe
    :type y: int
    :param universe: the universe of cells
    :type universe: np.ndarray
    """
    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    # The rules of Life
    if universe[x, y] and not 3 <= num_neighbours <= 5:
        return 0
    elif num_neighbours == 1:
        return 1
    return universe[x, y]

def pureSurvival(x, y, universe):
    """
    Compute one iteration of Life for one cell.
    :param x: x coordinate of cell in the universe
    :type x: int
    :param y: y coordinate of cell in the universe
    :type y: int
    :param universe: the universe of cells
    :type universe: np.ndarray
    """
    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    # The rules of Life
    if universe[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    return universe[x, y]

def wideSurvival(x, y, universe):#, multiplier):
    """
    Compute one iteration of Life for one cell.
    :param x: x coordinate of cell in the universe
    :type x: int
    :param y: y coordinate of cell in the universe
    :type y: int
    :param universe: the universe of cells
    :type universe: np.ndarray
    :param multiplier: multiplier for the weight of the second circle from the cell
    :type multiplier: float
    """
    multiplier = .5
    num_neighbours = (multiplier * sumSecondCircleEven(x, y, universe)) + np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y] 

    if universe[x, y] and not 3 <= num_neighbours <= 5:
        return 0
    elif num_neighbours == 1:
        return 1    
    
    return universe[x,y]

def spontLife(x, y, universe, index_universe):

    if universe[x,y]== 0:
        index_universe[x,y]=index_universe[x,y]+1
    elif universe[x,y]==1:
        index_universe[x,y]=0
                
    if  index_universe[x,y]>=20:
        if random.randint(1,20) == 1:
            universe[x,y] = 1
    elif  index_universe[x,y]>=40:
        if random.randint(1,10) == 1:
            universe[x,y] = 1
    elif  index_universe[x,y]>=60:    
        if random.randint(1,5) == 1:
            universe[x,y] = 1

    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    # The rules of Life
    if universe[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    return universe[x, y]

def spontDeath(x, y, universe, index_universe):
    """
    Compute one iteration of Life for one cell.
    :param x: x coordinate of cell in the universe
    :type x: int
    :param y: y coordinate of cell in the universe
    :type y: int
    :param universe: the universe of cells
    :type universe: np.ndarray
    """

    if universe[x,y]== 1:
        index_universe[x,y]=index_universe[x,y]+1
    elif universe[x,y]==1:
        index_universe[x,y]=0

    if  index_universe[x,y]>=10:
        if random.randint(1,5) == 1:
            universe[x,y] = 0
    elif  index_universe[x,y]>=20:
        if random.randint(1,5) == 1 or random.randint(1,5) == 2:
            universe[x,y] = 0
    elif  index_universe[x,y]>=30:    
        if random.randint(1,5) == 1 or random.randint(1,5) == 2 or random.randint(1,5) == 3:
            universe[x,y] = 0

    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    # The rules of Life
    if universe[x, y] and not 3 <= num_neighbours <= 5:
        return 0
    elif num_neighbours == 1:
        return 1
    return universe[x, y]

def sumSecondCircleEven(x, y, universe):
    num_neighbours = np.sum(universe[x - 2 : x + 3, y - 2 : y + 3]) - universe[x, y] 
    num_second_circle = num_neighbours - np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]

    return num_second_circle

def calcX(x_size):
    return int((universe_size[0]/2)-(x_size/2))

def calcY(y_size):
    return int((universe_size[0]/2)-(y_size/2))





surv_choice, seed_choice = setup()

print("Setting up ...")

universe = np.zeros((100, 100))
index_universe = np.zeros((100,100))
seed_array = np.array(seeds[seed_choice])
x_start, y_start = calcX(seed_array.shape[0]), calcY(seed_array.shape[1])
x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]
universe[x_start:x_end, y_start:y_end] = seed_array


#plt.imshow(universe, cmap='binary')
#plt.show()

# Create an identical copy of the universe, which will be the next generation.
#new_universe = np.copy(universe)

fig = plt.figure(dpi=200)

# Remove the axes for aesthetics
plt.axis('off')
ims = []


print("Running ...")
for i in range(200):
    # Add a snapshot of the universe, then move to the next generation
    ims.append((plt.imshow(universe, cmap='binary'),))
    universe = generation(universe, surv_choice, index_universe)

# Create the animation
im_ani = animation.ArtistAnimation(fig, ims, interval=700,
repeat_delay=1000, blit=True)

# Optional to save the animation
im_ani.save(seed_choice + surv_choice +'.gif', writer="pillow")

print("File saved as " + seed_choice + surv_choice +".gif")
