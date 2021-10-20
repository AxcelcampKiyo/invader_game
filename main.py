import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("殺してやる")

player = pygame.image.load("player.png")
playerX = 400
playerY = 200

X = 100
Y = 200

running = True


while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))

    # 押されたキーを調べる
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]:
        if playerX > 0:
            playerX -= 0.7

    if key_pressed[K_RIGHT]:
        if playerX < 800 - player.get_width():
            playerX += 0.7


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
