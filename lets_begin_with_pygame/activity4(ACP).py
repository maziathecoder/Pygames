import pygame
pygame.init()
SCREEN_WDITH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WDITH, SCREEN_HEIGHT))
pygame.display.set_caption('my first game screen')
flower_image = pygame.transform.scale(
    pygame.image.load('../flower.webp').convert_alpha(),(300, 300))
flower_rect = flower_image.get_rect(center=(SCREEN_WDITH // 2,
                                            SCREEN_HEIGHT // 2 - 30))
text = pygame.font.Font(None, 36).render('my first game screen', True,
                                        pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WDITH // 2,
                                  SCREEN_HEIGHT // 2 + 110))
BG_color = (58, 58, 58)
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.fill(BG_color)
        display_surface.blit(flower_image, flower_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
