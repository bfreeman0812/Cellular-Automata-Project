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
}

functions = { "pureSurvival", "diseaseSurvival"

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






def generation(universe, surv_choice):
    
    new_universe = np.copy(universe)

    # Simple loop over every possible xy coordinate.
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
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

def calcX(x_size):
    return int((universe_size[0]/2)-(x_size/2))

def calcY(y_size):
    return int((universe_size[0]/2)-(y_size/2))



















surv_choice, seed_choice = setup()
universe = np.zeros((100, 100))
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

for i in range(200):
    # Add a snapshot of the universe, then move to the next generation
    ims.append((plt.imshow(universe, cmap='binary'),))
    universe = generation(universe, surv_choice)

# Create the animation
im_ani = animation.ArtistAnimation(fig, ims, interval=700,
repeat_delay=1000, blit=True)

# Optional to save the animation
im_ani.save(seed_choice + surv_choice +'.gif', writer="pillow")