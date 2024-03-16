import pygame
import sys
import os
import random, time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def controll():
    global cur_move, direction, running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                cur_move = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                cur_move = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                cur_move = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                cur_move = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if cur_move == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if cur_move == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if cur_move == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if cur_move == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'


def moves():
    if direction == "RIGHT":
        if snake_pos[0] + 5 > WIDTH:
            snake_pos[0] = 0
        else:
            snake_pos[0] += 5
    if direction == "LEFT":
        if snake_pos[0] - 5 < 0:
            snake_pos[0] = 720
        else:
            snake_pos[0] -= 5
    if direction == "UP":
        if snake_pos[1] - 5 < 0:
            snake_pos[1] = 480
        else:
            snake_pos[1] -= 5
    if direction == "DOWN":
        if snake_pos[1] + 5 > HEIGHT:
            snake_pos[1] = 0
        else:
            snake_pos[1] += 5

def queue_go():
    global flag
    if flag == True:
        for pos in range(len(snake_stack) - 1):
            snake_stack[pos] = snake_stack[pos + 1]
        if len(snake_stack) != 0:
            snake_stack[-1] = snake_pos.copy()
    else:
        flag = True

def score():
    font = pygame.font.SysFont('arial', 18)
    text = font.render(f"Результат: {points}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_over():
    global points
    track.stop()
    track2 = pygame.mixer.Sound('12-нояб._-18.02_.mp3')
    track2.play()

    game_over_run = True
    screen.fill((0, 0, 0))

    ser_img = resource_path('maxresdefault.jpg')
    image = pygame.image.load(ser_img)
    image = pygame.transform.scale(image, (WIDTH - 100, HEIGHT)).convert()
    game_over_rect = image.get_rect()
    game_over_rect.center = WIDTH // 2, HEIGHT // 2
    while game_over_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over_run = False
                    points = 0
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    end = "end"

        if game_over_run:
            screen.blit(image, game_over_rect)
            pygame.draw.rect(screen, (0, 0, 0), game_over_rect, 1)
            pygame.display.update()
    track.play()

# Переменные для нашего экрана
WIDTH = 720
HEIGHT = 480
RED = (255, 0, 0)
FPS = 30
snake_pos = [720//2, 480//2]
snake_size = [10, 10]
difficulty = 25
points = 0
music = ""

# Движение игрока будем отслеживать в переменной cur_move
cur_move = "RIGHT"
direction = "RIGHT"

# Работа с дисплеем
pygame.init()
rect = pygame.Rect(snake_pos, snake_size)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ЗМЕЙКА")

# Переменные для изображения
apple_pos = [0, 0]
img_app = resource_path("967b98f78113900.png")
image = pygame.image.load(img_app)
image = pygame.transform.scale(image, (40, 40))
image.convert()
apple_rect = image.get_rect()
apple_pos[0] = random.randint(1, 720)
apple_pos[1] = random.randint(1, 480)
apple_rect.center = apple_pos[0], apple_pos[1]

# Переменные для нарастающего механизма змейки
snake_stack = [[720//2 - 140, 480//2], [720//2 - 120, 480//2], [720//2 - 100, 480//2],
               [720//2 - 90, 480//2], [720//2 - 80, 480//2], [720//2 - 70, 480//2],
               [720//2 - 60, 480//2], [720//2 - 50, 480//2], [720//2 - 40, 480//2],
               [720//2 - 30, 480//2], [720//2 - 20, 480//2], [720//2 - 10, 480//2]]

# MAIN THEME
track = pygame.mixer.Sound('toby_fox_-_megalovania_original_60999331.mp3')
track.play(loops=0)
track.set_volume(0.1)
track3 = pygame.mixer.Sound('441492.mp3')

running = True
flag = True
while running:
    rect = pygame.Rect(snake_pos, snake_size)

    # Создадим новое яблоко
    if abs(snake_pos[0] - apple_pos[0]) <= 15 and abs(snake_pos[1] - apple_pos[1]) <= 15:
        image = pygame.image.load(img_app)
        image = pygame.transform.scale(image, (40, 40))
        image.convert()
        apple_rect = image.get_rect()
        apple_pos[0] = random.randint(1, 720)
        apple_pos[1] = random.randint(1, 480)
        apple_rect.center = apple_pos[0], apple_pos[1]
        track3.play(1)
        track3.set_volume(100)


        # Удлиняем змея
        snake_stack.append(list(snake_pos))
        flag = False

        # Ускоряем змея
        difficulty += 3

        # Увеличиваем результат
        points += 1

    # Посмотрим какие кнопки нажал пользователь
    controll()

    queue_go()

    # Изменим направление движения у змеи
    moves()

    # Обновление экрана
    screen.fill(pygame.Color(0, 0, 0))

    # Настройки нашего изображения
    screen.blit(image, apple_rect)

    # Рисуем яблоко
    pygame.draw.rect(screen, (0, 0, 0), apple_rect, 1)

    # Рисуем змейку
    pygame.draw.rect(screen, RED, rect)

    # Прорисовываем движение змейки
    for pos in snake_stack:
        pygame.draw.rect(screen, RED, pygame.Rect([pos[0], pos[1]], snake_size))

    score()

    for pos in snake_stack:
        if snake_pos[0] == pos[0] and snake_pos[1] == pos[1]:
            game_over()


    # Обновление экрана
    pygame.display.update()
    pygame.time.Clock().tick(difficulty)

