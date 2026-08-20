#!/usr/bin/env python3
"""
---------------------
Conway's Game of Life
---------------------
Author: Eric Iniguez
Date: 2026 Aug 19
---------------------
I saw carykh's video of the Conway Multiverse and it inspired me to try and
recreate Conway's Game of Life by hand. It's certainly not the most optimal
implementation, though it's something I wanted to try for fun.
"""

import os
from time import sleep


def main():
    """
    Example of how to use conway.py as a library
    """

    # Define the seed cells as a list of tuples
    seed_cells = [(4,3),(4,4),(4,5)]

    run_game(seed_cells,
             board_width=8,
             board_height=8,
             cond_born=[3],
             cond_survive=[2,3],
             gen_delay=1)

def clear_screen():
    """
    Clears terminal screen
    """
    res = os.system('clear') if os.name != 'nt' else os.system('cls')
    return res

def print_board(board,board_width,board_height):
    """
    Prints the board state with a pretty border
    """
    def border():
        print(" "+" ".join('#' for _ in range(board_width)))

    border()
    for i in range(board_height):
        line_out = '#'
        for j in range(board_width):
            if board[i][j]:
                line_out += '* '
            else:
                line_out += '  '
        line_out = line_out[:-1]
        line_out += '#'
        print(line_out)
    border()

def get_neighbors(coord,board_width,board_height):
    """
    Returns a list of the 3-8 neighboring cells for a given cell at `coord`
    """
    ci, cj = coord

    neighbors = []

    # Look at cells 1 unit
    adj = [-1,0,1]
    for i in adj:
        for j in adj:
            ni,nj = ci+i,cj+j
            if (0 <= ni < board_height) and (0 <= nj < board_width):
                neighbors += [(ni,nj)]

    neighbors.remove(coord) # Remove coord from its list of neighbors
    return neighbors

def next_generation(board,board_width,board_height,cond_born,cond_survive):
    """
    Compute `board`'s next generation of cells
    """
    new_board = [row[:] for row in board] # Deep copy of board
    for i in range(board_height):
        for j in range(board_width):
            coord = (i,j)
            alive = board[i][j]

            # Determine conditions
            n_living = 0
            neighs = get_neighbors(coord,board_width,board_height)
            n_living = sum([board[ni][nj] for ni,nj in neighs])

            if alive and (n_living not in cond_survive):
                # Living cell dies
                new_board[i][j] = False
            if (not alive) and (n_living in cond_born):
                # Dead cell is born again
                new_board[i][j] = True
    board[:] = [row[:] for row in new_board]

def run_game(seed_cells,
             board_width=8,
             board_height=8,
             cond_born=[3],
             cond_survive=[2,3],
             gen_delay=1):
    """
    The pilot method that runs the game of life
    """

    if not seed_cells:
        print("No seed cells given.")

    board = [ [False for _ in range(board_width)] for _ in range(board_height)]

    for ax,ay in seed_cells:
        board[ax][ay] = True

    try:
        gen_count = 0
        while True:
            # Refresh screen
            clear_screen()
            print_board(board,board_width,board_height)
            print("Generation:",gen_count)

            # Compute next generation of cells
            next_generation(
                board,
                board_width,
                board_height,
                cond_born,
                cond_survive
            )
            gen_count += 1

            # Seconds to wait between generations
            sleep(gen_delay)
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt. Exiting...")
        exit()

if __name__ == '__main__':
    main()
