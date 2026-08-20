"""
---------------------
Conway's Game of Life
---------------------
Author: Eric Iniguez
Date: 2026 Aug 19
---------------------
I saw carykh's video of the Conway Multiverse and it inspired me to try and
recreate Conway's Game of Life by hand. It's certainly not the most optimal
implementation, though it's something to wanted to try for fun.
"""

import os
from time import sleep

BOARD_WIDTH = 9
BOARD_HEIGHT = 9

BOARD = [ [False for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# B3/S23
COND_BORN = [3]
COND_SURVIVE = [2,3]

# How many seconds to wait between generations
GEN_DELAY = 1

def main():
    alive_cells = [(3,4),(3,5),(3,6)]
    for c in alive_cells:
        ax, ay = c 
        BOARD[ax][ay] = True

    try:
        gen_count = 0
        while True:
            # Refresh screen
            clear_screen()
            print_board()
            print("Generation:",gen_count)

            # Compute next generation of cells
            next_generation()
            gen_count += 1

            # Wait between generations
            sleep(GEN_DELAY)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

def clear_screen():
    """
    Clears terminal screen
    """
    os.system('clear') if os.name != 'nt' else os.system('cls')

def print_board():
    """
    Prints the board state
    """
    def print_nums():
        print(" "+" ".join(str(i) for i in range(BOARD_WIDTH)))
    def border():
        print("="*(BOARD_WIDTH*2+1))

    print_nums()
    #border()
    for i in range(BOARD_HEIGHT):
        line_out = str(i)
        for j in range(BOARD_WIDTH):
            if BOARD[i][j]:
                line_out += '# '
            else:
                line_out += '  '
        line_out = line_out[:-1]
        line_out += str(i)
        print(line_out)
    #border()
    print_nums()

def get_neighbors(coord):
    """
    Returns a list of the 3-8 neighboring cells for a given cell at (coord)
    """
    ci, cj = coord

    neighbors = []

    # Look at cells 1 unit 
    adj = [-1,0,1]
    for i in adj:
        for j in adj:
            ni,nj = ci+i,cj+j
            if (0 <= ni < BOARD_HEIGHT) and (0 <= nj < BOARD_WIDTH):
                neighbors += [(ni,nj)]

    neighbors.remove(coord) # Remove coord from its list of neighbors
    return neighbors

def next_generation():
    """
    Compute the next generation of cells' living or dead state
    """
    new_board = [row[:] for row in BOARD] # Deep copy of BOARD
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            coord = (i,j)
            alive = BOARD[i][j]
            
            # Determine conditions
            n_living = 0
            neighs = get_neighbors(coord)
            n_living = sum([BOARD[ni][nj] for ni,nj in neighs])

            if alive and (n_living not in COND_SURVIVE):
                # Living cell dies
                new_board[i][j] = False
            if (not alive) and (n_living in COND_BORN):
                # Dead cell is born again
                new_board[i][j] = True
    BOARD[:] = [row[:] for row in new_board]

if __name__ == '__main__':
    main()

