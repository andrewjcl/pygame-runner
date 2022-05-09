import pygame
from sys import exit

""" Iniatialise """
pygame.init()                                       # Initialises pygame systems
screen = pygame.display.set_mode((800, 400))        # Sets main window
pygame.display.set_caption('Runner')                # Sets window title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 35)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

# Game event loop
while True:
    # Check for key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if player_rect.collidepoint(mouse_pos):
                print('** player **')
            elif snail_rect.collidepoint(mouse_pos):
                print('** snail **')
            elif mouse_pos[1] < 300:
                print('** sky **')
            else:
                print('** ground **')

    # Blit images
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 10)
    
    screen.blit(score_surf, score_rect)
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)



    pygame.draw.line(screen, 'Gold', (400, 150), pygame.mouse.get_pos(), 2)

    # Update positions
    snail_rect.x -= 2
    if snail_rect.right < 0: snail_rect.right = 800



    # if player_rect.colliderect(snail_rect):
    #     print('COLLISION!')


    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pos())


    pygame.display.update()
    clock.tick(60)


    # 1:23:25
    # https://www.youtube.com/watch?v=AY9MnQ4x3zk