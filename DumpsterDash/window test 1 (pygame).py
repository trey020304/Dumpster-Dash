import pygame
import sys

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Our Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        
    screen.fill((0,100,255))
    
    pygame.display.update()