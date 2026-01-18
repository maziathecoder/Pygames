import pygame
import random
#initialize pygame
pygame.init()
# custom event IDs for color change events
sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2
# define asic colors uing pygame.color
#bg colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
# sprite colors
WHITE = pygame.Color('white')
LIGHTPINK = pygame.Color('lightpink')
PINK = pygame.Color('pink')
DARKPINK = pygame.Color(199, 21, 133)
# sprite class represents the moving object
class sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        # create the sprites surface with dimensions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # get the sprite's srect defining its position and size
        self.rect = self.image.get_rect()
        #set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        #method to update the sprites position
    def update(self):
        #move the sprite by its velocity
        self.rect.move_ip(self.velocity)
        # flag to track if the sprites hits a boundary
        boundary_hit = False
        # check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True#check for collision with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
                self.velocity[1] = -self.velocity[1]
                boundary_hit = True
        # if boundary was hit, post events to change colors
        if boundary_hit:
             pygame.event.post(pygame.event.Event(background_color_change_event))
    #method to change the sprites color
    def change_color(self):
         self.image.fill(random.choice([WHITE, LIGHTPINK, PINK, DARKPINK]))
#function to change the bg color
def change_background_color():
     global bg_color
     bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
#create a group to hold the sprite
all_sprite_list = pygame.sprite.Group()
#instantiate the sprite
sp1 = sprite(WHITE, 20, 30)
#randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
# add the sprite to the group
all_sprite_list.add(sp1)
#create the game window
screen = pygame.display.set_mode((500,400))
#set the initialbg color
bg_color = BLUE
#apply the bg color
screen.fill(bg_color)
#game loop control flag
exit = False
#create a clock object to control frame rate
clock = pygame.time.Clock()
#mian game loop
while not exit:
    #event handling loop
    for event in pygame.event.get():
        #if the windows close button is clicked, exit the game
        if event.type == pygame.QUIT:
            exit = True
        # if the sprite color change event is triggered, change te sprite's color
        elif event.type == sprite_color_change_event:
            sp1.change_color()
        # if the g color change event is triggered, change the bg color
        elif event.type == background_color_change_event:
             change_background_color()
    # update all sprites
    all_sprite_list.update()
    #fill the screen with the current bg clor
    screen.fill(bg_color)
    #draw all sprites to the screen
    all_sprite_list.draw(screen)
    # rfresh the display
    pygame.display.flip()
    # limit the frame rate to 240 fps
    clock.tick(240)
#unintialize all pygame madules and close the window
pygame.quit()
