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

- Function score is following the player progress and display it on the screen.

```
def game_over():
  pass
```

- Function game_over creates the game_over screen that will appear if snake is dead.

### How to create .exe file?

In file setyp.py, with a help of the library cx_Freeze, we create .exe file from snake.py in main folder of the project.

```
import cx_Freeze
```

### How the main algohrithm is realized.

Firstly we draw rectangle on the screen, this figure will represent our snake. Then when the rectangle (snake) collects an apple we fix the snake position and using current coordinates we create a new rectangle which stops for a moment and then this new reactangle will be following previeous rectangle list. With this algohrithm we change the snake lenght.
