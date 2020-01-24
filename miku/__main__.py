import pygame
import miku
import miku.sprite
import sys


pygame.init()
screen = pygame.display.set_mode((miku.WINDOW_WIDTH, miku.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Miku")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    miku.sprite.sprite_group.update()
    miku.sprite.sprite_group.draw(screen)
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)

