import pygame
# initialize pygame
pygame.init()
# screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites Game")
# colors
WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
RED = pygame.Color("red")
# clock
clock = pygame.time.Clock()
# sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
# create sprites
player = Player(BLUE, 40, 30, 100, 150)
enemy = Player(RED, 50, 40, 400, 200)  # no controls
# sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    # update only player with controls
    player.update(keys)
    # background
    screen.fill(WHITE)
    # draw sprites
    all_sprites.draw(screen)
    # update display
    pygame.display.flip()
    # FPS
    clock.tick(60)
pygame.quit()