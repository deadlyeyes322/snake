# Snake

This is my snake project, which I wrote on Python.

My project consists of two files. First file is the game algohrithm. Second file is creating .exe file.

## Algohrithm

For my project we need some libraries
```
import pygame
import sys
import os
import random, time
```

- Pygame is main library that we need, It creates screen for the game and updates events on the screen.

- Sys and Os help us to the one function.
```
def resource_path(relative_path):
  pass
```
  &nbsp; &nbsp; &nbsp; &nbsp; This function helps us to load needed files for the game.

- Random and Time are Standart Python libraries, that we need to gane algohrithm.

### Game

Player controlled the snake. Snake can move in 4 directions (Up, Down, Left, Right). Player needs to collect apples, that randomly spawn on the screen, library Random help us to randomly generate apples.

### Functions

```
def controll():
  pass
```

- First function is controll. It capture player inputs and convert them to the variables.

```
def moves():
  pass
```

- Function moves change player coordinates on the screen.

```
def queue_go():
  pass
```

- Function queue_go is changing snake length.

```
def score():
  pass
```

- Function score is following player progress and display it on the screen.

```
def game_over():
  pass
```

- Function game_over needed to create the game_over screen, that will appear if snake is dead.

### Converting in .exe file

In file setyp.py, with help library cx_Freeze, we convert .exe file from snake.py, that will be created in main folder our project.

```
import cx_Freeze
```

### How realized main algohrithm. 

I creates one Rect, this figure is snake. When the rect is collecting one apple, I fix the snake position and on the currently coordinates I create another one Rect, which I stop for a moment and then the new Rect will be follow previeous Rect list. With this algohrithm we change snake lenght
