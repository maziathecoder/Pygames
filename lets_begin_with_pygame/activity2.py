import pygame
pygame.init()
SCREEN_WDITH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WDITH, SCREEN_HEIGHT))
pygame.display.set_caption('adding image and background image')
background_image = pygame.transform.scale(  
    pygame.image.load('backgruond.png').convert(),
    (SCREEN_WDITH, SCREEN_HEIGHT))
penguin_image = pygame.transform.scale( 
    pygame.image.load('hello penguin.png').convert_alpha(),(200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WDITH // 2,
                                              SCREEN_HEIGHT // 2 - 30))
text = pygame.font.font(None, 36).render('Hello world ', True,
                                         pygame.color('black'))
text_rect = text.get_rect(center=(SCREEN_WDITH // 2,
                                  SCREEN_HEIGHT // 2 + 110))
def game_loop():
    clock = pygame.time.clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
