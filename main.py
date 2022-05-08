import pygame
from sys import exit

def snail_wrap(pos_x):
    if pos_x < -80:
        return 800
    return pos_x



""" Iniatialise """
pygame.init()                                       # Initialises pygame systems
screen = pygame.display.set_mode((800, 400))        # Sets main window
pygame.display.set_caption('Runner')                # Sets window title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 35)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game text', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail2_surface = pygame.image.load('graphics/snail/snail1_red.png').convert_alpha()
snail_x_pos = 600
snail2_x_pos = 1200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, 264))
    screen.blit(snail2_surface, (snail2_x_pos, 264))
    snail_x_pos -= 2
    snail2_x_pos -= 4




    snail_x_pos = snail_wrap(snail_x_pos)
    snail2_x_pos = snail_wrap(snail2_x_pos)

    pygame.display.update()
    clock.tick(60)




    # https://www.youtube.com/watch?v=AY9MnQ4x3zk