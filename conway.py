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

BOARD_SIZE = 9
BOARD_WIDTH = BOARD_SIZE
BOARD_HEIGHT = BOARD_SIZE

BOARD = [ [False for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# B3/S23
COND_BORN = [3]
COND_SURVIVE = [2,3]

# How many seconds to wait between generations
GEN_DELAY = 1

def main():
    alive_cells = [(3,4),(3,5),(3,6)]
    for ax,ay in alive_cells:
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
    def border():
        print("="*(BOARD_WIDTH*2+1))

    border()
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if BOARD[i][j]:
                print(' #',end='')
            else:
                print('  ',end='')
        print()
    border()

def get_neighbors(coord):
    """
    Returns a list of the 3-8 neighboring cells for a given cell at (coord)
    """
    cx, cy = coord

    neighbors = []

    # Look at cells 1 unit 
    adj = [-1,0,1]
    for x in adj:
        for y in adj:
            nx,ny = cx+x,cy+y
            if nx < 0 or ny < 0 or nx >= BOARD_WIDTH or ny >= BOARD_HEIGHT:
                continue # Skip if neighbor doesn't exist
            neighbors += [(nx,ny)]

    neighbors.remove(coord) # Remove coord from its list of neighbors
    return neighbors

def next_generation():
    """
    Compute the next generation of cells' living or dead state
    """
    new_board = BOARD
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            coord = (i,j)
            alive = BOARD[i][j]
            
            # Determine conditions
            n_living = 0
            for neigh in get_neighbors(coord):
                nx,ny = neigh
                if BOARD[nx][ny]:
                    n_living += 1

            if alive and (n_living not in COND_SURVIVE):
                # Living cell dies
                new_board[i][j] = False
            elif n_living in COND_BORN:
                # Dead cell is born again
                new_board[i][j] = True
    BOARD[:] = new_board

if __name__ == '__main__':
    main()
