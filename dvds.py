import pygame
import sys
pygame. init( )

speed = [2, 1]

size = width, height= 480, 270

screen = pygame.display.set_mode(size)
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock( )

logo = pygame.image.load("dvd.png")
rect = logo.get_rect()

fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if rect.left < 0:
        speed[0] = -speed[0]
    if rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0:
        speed[1] = -speed[1]
    if rect.bottom > height:
        speed[1] = -speed[1]
    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logo, rect)
    pygame.display.update( )
    clock. tick( fps )