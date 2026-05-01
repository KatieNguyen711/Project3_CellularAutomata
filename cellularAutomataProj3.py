# Game of Life rules: 
# For a space that is alive
# 1. Each cell with one or no neighbors dies, as if by solitude.
# 2. Each cell with four or more neighbors dies, as if by overpopulation.
# 3. Each cell with two or three neighbors survives.
# For a space that is dead
# 4. Each cell with three neighbors becomes populated.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid size
N = 50

# Create random grid (if the cell is 0, it is dead; if it is 1, it is alive)
grid = np.random.choice([0, 1], size=(N, N))

# Goes through each cell and counts how many cells that surround the current cell are alive
# Based on the total, the current cell's state changes
def update(frame):
    global grid
    new_grid = grid.copy()

    for i in range(N):
        for j in range(N):
            # get directions
            left = (i - 1) % N
            right = (i + 1) % N
            above = (j + 1) % N
            below = (j - 1) % N

	    # Counts alive cells around current cell
            total = int((
                grid[i, below] 
		+ grid[i, above] 
		+ grid[left, j] 
		+ grid[right, j] 
		+ grid[left, below] 
		+ grid[left, above] 
		+ grid[right, below] 
		+ grid[right, above]
            ))
	    
	    

            # If cell is alive and total alive neighbors are less than 2 or greater than 3, it dies
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
	    # If cell is dead and total alive neighbors equal to 3, it becomes alive 
            else:
                if total == 3:
                    new_grid[i, j] = 1

    grid = new_grid
    mat.set_data(grid)
    return [mat]

# Set up the plot
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='binary')
plt.title("Cellular Automata - Game of Life")

# Animate
anim = animation.FuncAnimation(fig, update, interval=500, cache_frame_data=False)

plt.show()

