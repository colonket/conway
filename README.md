# Conway's Game of Life

Felt inspired after watching caryhk's ["The Conway Multiverse"](https://www.youtube.com/watch?v=QK_KZv-YyOc) recreate Conway's Game of Life without an LLM agent.

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

I've seen Conway's Game of Life for many years now and I have never tried making it until now. I was on a mini vacation and wanted to recapture that feeling of being a computer science undergraduate before the advent of LLMs and write fun code by hand.

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

In the end, my code was all handwritten except for the line that Gemma fixed. I consulted Gemma4 when I was stuck at a point where previously I would've reached out to a friend or spent hours on Stack Overflow for help.

### Rambling

Younger me would be proud that I was able to make it that far without needing help. Present me feels proud that I made younger me proud, and continues to grapple with how new generations of programming learners will have their skills affected by LLMs. 

When I've taught high schoolers how to write Python, I've seen them immediately copy and paste LLM output for problems as simple as "How do you make a for loop?". They get stuck and ask me to fix the code when they have no idea what went wrong or what they were trying to do.

LLMs are no doubt useful, I use them frequently myself for programming and system adminstration tasks. I review the LLM output and am usually able to catch bugs or errors before I run its code because I have enough experience without LLMs. 

There are times where I've felt like I just wanted to copy and paste repeatedly because it was the most convenient way to complete a task even if I didn't understand what was going on. This is what happens when programmers don't want to engage their problem-solving skills and just want to click a few buttons until the LLM gives them the output they want.

Where do LLMs fit in the future of education? I would be a hypocrite to tell students to not use LLMs for coding. Apart from coding tasks, I am against using LLMs to write on your behalf. Your words have weight and meaning, and become hollow when you allow the token prediction machine that plagiarized the Internet to speak for you. Generative art is also plagiarism of many artists' works taken without their consent. But what about generating SVGs? What about having LLMs generate the code that builds an SVG graphic? What makes plagiarising decades of human-written code okay but plagiarising art not okay? I suppose code is not considered art in the same way that your personal writing is a language art and photos and drawings are a visual art. I apply LLMs to code-generation as a tool to give me what I need to fulfill a programming or system task. When you apply AI to arts of language, visual, or audio, you're treating that art as a task to be fulfilled. When you make an AI model generate a digital painting of a forest, you're treating the production of the digital painting as a means to an end. There is no human that felt inspired and applied their years of experience and motor skills to manipulate paint and a paint brush to illustrate a vision from their head onto a canvas. It is simply a soulless array of pixels on a screen. Perhaps the soulless array of pixels speaks to you, perhaps it inspires you.

There are people who feel a strong connection to their LLM Chatbot "romantic partners". This I would argue is not a valid, consensual relationship, it is an illusion of a relationship. It is an algorithm predicting the next token to generate based on the previously existing tokens. Given the prompt and conversation, the LLM will generate the words that a partner would give you if there in fact a romantic partner there. You have the texts of a partner, but the partner is not there. Is that really a relationship? I would not consider it so.

All this to say, I challenged myself to write Conway's Game of Life as a return to the joy I felt from programming before vibe-coding became the norm. I feel conflicted that I appreciate the utility of LLMs while feeling frustrated that people are using LLMs irresponsibly to create lack-luster products. The integrity of creators is doubted as consumers have to question whether the creator genuinely created the content themselves or they are passing off an LLMs work as their own.

Anyways, enjoy my implementation of Conway's Game of Life.

