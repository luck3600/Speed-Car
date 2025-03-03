import pygame
import random

#Настройки окна
WIDTH = 300
HEIGHT = 500
FPS = 60

#Настройка цвета
WHITE = (255, 255, 255)
RED = (241, 58, 19)
BLACK = (0, 0, 0)

#Инициализация
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Стартовое положение машинки по x и y
xpos = 130
ypos = 405

# Параметры машинки
CARWIDTH = 40
CARHEIGHT = 70
car = pygame.Rect(xpos, ypos, CARWIDTH, CARHEIGHT)
car_img = pygame.image.load('car.jpg').convert()
car_enemy_img = pygame.image.load('carenemy.jpg').convert()

SPEED = 2
y_enemy = 0 - CARHEIGHT
position = random.randint(1, 3)
if position == 1:
    x_enemy = 10
elif position == 2:
    x_enemy = 130
elif position == 3:
    x_enemy = 250

car_enemy = pygame.Rect(x_enemy, y_enemy, CARWIDTH, CARHEIGHT)
font = pygame.font.SysFont('arial', 24)

points = 0
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                if car.left > 10:
                    car.left -= 120
            if i.key == pygame.K_RIGHT:
                if car.left < 250:
                    car.left += 120
    # Изменение положения вражеской машинки при выходе за экран
    if car_enemy.top >= HEIGHT + CARHEIGHT:
        points += 1
        SPEED += 0.7
        car_enemy.top = 0 - CARHEIGHT
        position = random.randint(1, 3)
        if position == 1:
            car_enemy.left = 10
        elif position == 2:
            car_enemy.left = 130
        elif position == 3:
            car_enemy.left = 250
    else:
        # Прибавление скорости
        car_enemy.top += SPEED

    # Отрисовка объектов
    screen.fill(WHITE)
    text = font.render("Обогнанно машин: " + str(points), 0, (0,0,0))
    screen.blit(text, (10,10))
    pygame.draw.line(screen, (0,0,0), [100,50] ,[100, 500])
    pygame.draw.line(screen, (0,0,0), [200,50] ,[200, 500])
    screen.blit(car_enemy_img, (car_enemy.left, car_enemy.top))
    screen.blit(car_img, (car.left, car.top))
    pygame.display.update()

    # Обработка столкновения
    if car.colliderect(car_enemy):
           running = False

    clock.tick(FPS)
pygame.quit()