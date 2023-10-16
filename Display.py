import pygame

pygame.init()
font = pygame.font.Font("freesansbold.ttf", 40)
display = pygame.display.set_mode((1920, 1080))
pygame.display.flip()
pygame.display.set_caption("Game Alpha 4.0")

def Update():
    pygame.display.update()