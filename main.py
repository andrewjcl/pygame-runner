import pygame
from sys import exit

pygame.init()                                       # Initialises pygame systems
screen = pygame.display.set_mode((800, 400))        # Sets main window
pygame.display.set_caption('Runner')                # Sets window title
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))
    pygame.display.update()
    clock.tick(60)

    # Current time 28:16
    # https://www.youtube.com/watch?v=AY9MnQ4x3zk