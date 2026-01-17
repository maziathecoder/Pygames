import pygame
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Screen")
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
font = pygame.font.Font(None, 48)
running = True
while running:
    screen.fill(white)
    pygame.draw.rect(screen, blue, [200, 150, 400, 300])
    text = font.render("Hello Pygame!", True, red)
    text_rect = text.get_rect(center=(screen_width/2, 100))
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
sys.exit()