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

