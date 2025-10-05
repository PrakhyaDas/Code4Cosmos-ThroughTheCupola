import pygame, sys

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Code4Cosmos: Through the Cupola")

# Placeholder images
earth = pygame.Surface((WIDTH, HEIGHT))
earth.fill((0, 100, 255))
cupola = pygame.Surface((300, 200))
cupola.fill((200, 200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(earth, (0, 0))
    screen.blit(cupola, (WIDTH//3, HEIGHT//4))
    pygame.display.flip()

pygame.quit()