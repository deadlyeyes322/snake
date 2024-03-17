# Snake

This is my snake project, which I wrote on Python.

My project consists of two parts. Firstly, creation game algohrithm. Secondly, changing snake.py file to .exe file.

## Algohrithm

Firstly, for my project we needed some libraries
```
import pygame
import sys
import os
import random, time
```

- Pygame is main library that we need, It created screen for game and updated events on this screen.

- Sys and Os we need to create one function.
```
def resource_path(relative_path):
  pass
```
- This function help us to upload needed files for game.

- Random and time is Standart Python library, that we need to gane algohrithm

### Game

Player controlled snake. He can go in 4 directions (Up, Down, Left, Right). Player need to collect apples, that randomly spawn on the screen, library random help us to randomly generation apples.

### Functions

```
def controll():
  pass
```

- First function is controll. It follow player inputs and convert them to variables.

```
def moves():
  pass
```

- Function moves change position player snake in space.

```
def queue_go():
  pass
```

- Function queue_go change lentgh player snake.

```
def score():
  pass
```

- Function score is following player progress and display it on screen.

```
def game_over():
  pass
```

- Function game_over needed to create game_over screen, that appear if snake is dead.

### Converting in .exe file

In file setyp.py, with help library cx_Freeze, we convert .exe file from snake.py, that will be created in main folder our project.

```
import cx_Freeze
```

### How realized main algohrithm. 

I create one Rect, this figure is our snake. When this rect collect one apple, I fix the position snake and on currently coordination I create another one Rect, which I stop for a moment and then this new Rect will be follow our previeous Rect list. With this algohrithm we change snake lenght
