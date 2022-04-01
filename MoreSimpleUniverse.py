import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def generation(universe):
    
    new_universe = np.copy(universe)

    # Simple loop over every possible xy coordinate.
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            new_universe[i,j] = survival(i, j, universe)

    # Set universe to be equal to new_universe.
    universe = np.copy(new_universe)
    return universe

def survival(x, y, universe):
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



universe = np.zeros((6, 6))

beacon = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

universe[1:5, 1:5] = beacon


#plt.imshow(universe, cmap='binary')
#plt.show()

# Create an identical copy of the universe, which will be the next generation.
#new_universe = np.copy(universe)

fig = plt.figure(dpi=200)

# Remove the axes for aesthetics
plt.axis('off')
ims = []

for i in range(30):
    # Add a snapshot of the universe, then move to the next generation
    ims.append((plt.imshow(universe, cmap='binary'),))
    universe = generation(universe)

# Create the animation
im_ani = animation.ArtistAnimation(fig, ims, interval=700,
repeat_delay=1000, blit=True)

# Optional to save the animation
im_ani.save('Picture\Beacon.gif', writer="pillow")

