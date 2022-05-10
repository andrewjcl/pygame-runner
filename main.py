from operator import truediv
import pygame
from sys import exit

""" Iniatialise """
pygame.init()                                       # Initialises pygame systems
screen = pygame.display.set_mode((800, 400))        # Sets main window
pygame.display.set_caption('Runner')                # Sets window title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 35)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (80, 80, 80))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (835, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0
player_grounded = True

# Game event loop
while True:
    # Check for key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                player_gravity = -12
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -12

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surf, score_rect)

        # Snail
        snail_rect.x -= 4
        if snail_rect.right < 0: snail_rect.right = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 0.5
        player_rect.y += player_gravity
        
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            # player_gravity = 0

        screen.blit(player_surf, player_rect)

        # Collision

        if player_rect.colliderect(snail_rect):
            game_active = False

    else:  # if not game_active
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)
    print(player_gravity)


    # 1:53:00
    # https://www.youtube.com/watch?v=AY9MnQ4x3zk