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

BOARD = [ [[(i,j),False] for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]

# B3/S23
COND_BORN = [3]
COND_SURVIVE = [2,3]

# How many seconds to wait between generations
GEN_DELAY = 0.5

def main():
    alive_cells = [(1,1),(1,2),(1,3)]
    for a in alive_cells:
        update_cell(a,True)

    try:
        gen_count = 0
        while True:
            # Refresh screen
            os.system('clear') if os.name != 'nt' else os.system('cls')
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
    #test_cells = [(1,1),(0,0),(0,9),(9,0),(9,9)]
    #for t in test_cells:
        #n = get_neighbors(t)
        #print(t,len(n),n)

def print_board():
    """
    Prints the board state
    """
    def border():
        print("="*(BOARD_WIDTH*2+1))

    border()
    for row in BOARD:
        for _, is_alive in row:
            if is_alive:
                print(' #',end='')
            else:
                print('  ',end='')
        print()
    border()

def get_cells():
    """
    Returns a list of all cells in the board
    """
    cells = []
    for row in BOARD:
        for c in row:
            cells += [c]
    return cells

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

def update_cell(coord,state):
    """
    Update the living state of a cell at the given coordinate
    """
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if BOARD[i][j][0] == coord:
                BOARD[i][j][1] = state

def get_cell_state(coord):
    """
    Get the living state of a cell at the given coordinate
    """
    i,j = coord
    return BOARD[i][j][1]

def next_generation():
    """
    Compute the next generation of cells' living or dead state
    """
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            coord, alive_state = BOARD[i][j]

            # Determine conditions
            n_alive = 0
            #print(coord,'=>',end=' ')
            for neigh in get_neighbors(coord):
                #print(neigh,end=' ')
                if get_cell_state(neigh):
                    n_alive += 1
            #print()

            if alive_state and n_alive not in COND_SURVIVE:
                # Living cell dies
                update_cell(coord, False)
            elif n_alive in COND_BORN:
                # Dead cell is born again
                update_cell(coord, True)

if __name__ == '__main__':
    main()
