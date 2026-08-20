# Conway's Game of Life

After watching caryhk's ["The Conway Multiverse"](https://www.youtube.com/watch?v=QK_KZv-YyOc) I felt inspired to recreate Conway's Game of Life.
I've seen Conway's Game of Life since many years ago and I have never tried making it until now.

## Usage
You can run `conway.py` to see a simple blinker shape with:
```bash
python3 conway.py
```

```
 # # # # # # # #
#               #
#               #
#               #
#        *      #
#        *      #
#        *      #
#               #
#               #
 # # # # # # # #
Generation: 3
B3/S23
Press ^C to exit
```


You can import the main script into another file to run your own simulations like so:
```python3
# glider.py
import conway
# 16x16 Board with a glider shape, B3/S23 seed, and 0.25 sec generation delay
seed_cells = [(3,1),(3,2),(3,3),(2,3),(1,2)]
conway.run_game(
  seed_cells,
  board_width=16,
  board_height=16,
  cond_born=[3],
  cond_survive=[2,3],
  gen_delay=0.25
)
```

```bash
python3 glider.py
```

```
 # # # # # # # # # # # # # # # #
#                               #
#                               #
#                               #
#                               #
#                               #
#                               #
#                               #
#                               #
#                               #
#                               #
#                               #
#                        *      #
#                          *    #
#                      * * *    #
#                               #
#                               #
 # # # # # # # # # # # # # # # #
Generation: 40
B3/S23
Press ^C to exit
```

## Background

This was also a fun challenge for me to write code without a coding agent like how we used to before LLMs became prevalent.
I was doing fine until I kept encountering a bug where the board state was being modified in the middle of the next generation being computed.
I asked my local gemma4:e4b model to point any issues in my code.

Gemma4 pointed out that I was creating a shallow copy of the board state with:

```python3
new_board = BOARD[:]
```

so any time I modified `new_board` I was actually modifying the original arrays within `BOARD`.

Gemma4 recommended I fix it by using a *deep copy* instead:

```python3
new_board = [row[:] for row in BOARD]
```

In the end, my code was still handwritten except for the line that Gemma fixed. I consulted Gemma4 when I was stuck at a point where
previously I would've reached out to a friend or spent hours on Stack Overflow for help.

