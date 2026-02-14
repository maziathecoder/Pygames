import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies Collision Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 40)
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 6
enemy_size = 50
num_enemies = 7
enemies = []
for i in range(num_enemies):
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = random.randint(0, HEIGHT // 2)
    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size))
player = pygame.Rect(player_x, player_y, player_size, player_size)
score = 0
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    player.x = max(0, min(player.x, WIDTH - player_size))
    player.y = max(0, min(player.y, HEIGHT - player_size))
    pygame.draw.rect(screen, WHITE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, WIDTH - enemy_size)
            enemy.y = random.randint(0, HEIGHT // 2)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()
pygame.quit()