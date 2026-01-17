import pygame
def main():
    pygame.init()
    screen_wdith, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_wdith, screen_height))
    pygame.display.set_caption('color changing sprite')
    colors = { 
        'red': pygame.color('red'),
        'green': pygame.color('green'),
        'blue': pygame.color('blue'),
        'yellow': pygame.color('yellow'),
        'white': pygame.color('white')
    }
    current_color = colors['white']
    x, y = 30, 30
    sprite_wdith, sprite_height = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        x = min(max(0,x), screen_wdith - sprite_wdith)
        y = min(max(0, y), screen_height - screen_height)
        if x == 0: current_color = colors['blue']
        elif x == screen_wdith - sprite_wdith: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']
        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_wdith, sprite_height))
        pygame.display.flip()
        clock.tick(90)
        pygame.quit()
if __name__ == "__main__":
    main()
