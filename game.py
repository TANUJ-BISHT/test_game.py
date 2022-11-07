import pygame , random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('TOP DOWN TEST GAME')
game_icon = pygame.image.load('test_game/assets/game_icon.png').convert_alpha()
pygame.display.set_icon(game_icon)

player = pygame.image.load('test_game/assets/player.png').convert_alpha()
player_rect = player.get_rect(center = (590,350))

ground = pygame.image.load('test_game/assets/ground.png').convert_alpha()
ground_rect = ground.get_rect(center = (0,0))
game_active = True

class trees(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__() 
        self.image = pygame.image.load('test_game/assets/tree.png')
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
trees_group = pygame.sprite.Group()
for i in range(20):
    new_tree = trees(random.randrange(0,1280),random.randrange(0,720))
    trees_group.add(new_tree)
def tree_pos_y(change_pos):
    for i in trees_group:
        i.rect.y += change_pos
def tree_pos_x(change_pos):
    for i in trees_group:
        i.rect.x += change_pos

def change_player_size(walk_list):
    just_list = []
    for walk in walk_list:
        walk = pygame.transform.scale(walk,(200,200))
        just_list.append(walk)
    return(just_list)

walk_up = []
walk_up.append(pygame.image.load('test_game/assets/walk/walk up1.png').convert_alpha())
walk_up.append(pygame.image.load('test_game/assets/walk/walk up2.png').convert_alpha())
walk_up.append(pygame.image.load('test_game/assets/walk/walk up3.png').convert_alpha())
walk_up.append(pygame.image.load('test_game/assets/walk/walk up4.png').convert_alpha())
walk_down = []
walk_down.append(pygame.image.load('test_game/assets/walk/walk down1.png').convert_alpha())
walk_down.append(pygame.image.load('test_game/assets/walk/walk down2.png').convert_alpha())
walk_down.append(pygame.image.load('test_game/assets/walk/walk down3.png').convert_alpha())
walk_down.append(pygame.image.load('test_game/assets/walk/walk down4.png').convert_alpha())
walk_right = []
walk_right.append(pygame.image.load('test_game/assets/walk/walk right1.png').convert_alpha())
walk_right.append(pygame.image.load('test_game/assets/walk/walk right2.png').convert_alpha())
walk_right.append(pygame.image.load('test_game/assets/walk/walk right3.png').convert_alpha())
walk_right.append(pygame.image.load('test_game/assets/walk/walk right4.png').convert_alpha())
walk_left = []
walk_left.append(pygame.image.load('test_game/assets/walk/walk left1.png').convert_alpha())
walk_left.append(pygame.image.load('test_game/assets/walk/walk left2.png').convert_alpha())
walk_left.append(pygame.image.load('test_game/assets/walk/walk left3.png').convert_alpha())
walk_left.append(pygame.image.load('test_game/assets/walk/walk left4.png').convert_alpha())
walk_up = change_player_size(walk_up)
walk_down = change_player_size(walk_down)
walk_right = change_player_size(walk_right)
walk_left = change_player_size(walk_left)


walk_idle_up = []
walk_idle_up.append(pygame.image.load('test_game/assets/idle/idle up1.png').convert_alpha())
walk_idle_up.append(pygame.image.load('test_game/assets/idle/idle up2.png').convert_alpha())
walk_idle_up.append(pygame.image.load('test_game/assets/idle/idle up3.png').convert_alpha())
walk_idle_up.append(pygame.image.load('test_game/assets/idle/idle up4.png').convert_alpha())
walk_idle_down = []
walk_idle_down.append(pygame.image.load('test_game/assets/idle/idle down1.png').convert_alpha())
walk_idle_down.append(pygame.image.load('test_game/assets/idle/idle down2.png').convert_alpha())
walk_idle_down.append(pygame.image.load('test_game/assets/idle/idle down3.png').convert_alpha())
walk_idle_down.append(pygame.image.load('test_game/assets/idle/idle down4.png').convert_alpha())
walk_idle_right = []
walk_idle_right.append(pygame.image.load('test_game/assets/idle/idle right1.png').convert_alpha())
walk_idle_right.append(pygame.image.load('test_game/assets/idle/idle right2.png').convert_alpha())
walk_idle_right.append(pygame.image.load('test_game/assets/idle/idle right3.png').convert_alpha())
walk_idle_right.append(pygame.image.load('test_game/assets/idle/idle right4.png').convert_alpha())
walk_idle_left = []
walk_idle_left.append(pygame.image.load('test_game/assets/idle/idle left1.png').convert_alpha())
walk_idle_left.append(pygame.image.load('test_game/assets/idle/idle left2.png').convert_alpha())
walk_idle_left.append(pygame.image.load('test_game/assets/idle/idle left3.png').convert_alpha())
walk_idle_left.append(pygame.image.load('test_game/assets/idle/idle left4.png').convert_alpha())
walk_idle_up = change_player_size(walk_idle_up)
walk_idle_down = change_player_size(walk_idle_down)
walk_idle_right = change_player_size(walk_idle_right)
walk_idle_left = change_player_size(walk_idle_left)

current_frame = 0
current_direction = 1

def player_walk_animation(direction):
    global current_frame

    if direction == 1:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_up[int(current_frame)],player_rect)

    elif direction == 2:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_down[int(current_frame)],player_rect)
    elif direction == 3:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_right[int(current_frame)],player_rect)
    elif direction == 4:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_left[int(current_frame)],player_rect)

def player_idle_animation(direction):
    global current_frame

    if direction == 1:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_idle_up[int(current_frame)],player_rect)

    elif direction == 2:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_idle_down[int(current_frame)],player_rect)
    elif direction == 3:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_idle_right[int(current_frame)],player_rect)
    elif direction == 4:
        current_frame += (0.1)
        if current_frame >= 4:
            current_frame = 0
        screen.blit(walk_idle_left[int(current_frame)],player_rect)

while game_active:
    screen.fill('sky blue')
    screen.blit(ground,ground_rect)
    trees_group.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ground_rect.y += 3
        tree_pos_y(3)
        player_walk_animation(1)
        current_direction = 1
    elif keys[pygame.K_DOWN]:
        ground_rect.y -= 3
        tree_pos_y(-3)
        player_walk_animation(2)
        current_direction = 2
    elif keys[pygame.K_RIGHT]:
        ground_rect.x -= 3
        tree_pos_x(-3)
        player_walk_animation(3)
        current_direction = 3
    elif keys[pygame.K_LEFT]:
        ground_rect.x += 3
        tree_pos_x(3)
        player_walk_animation(4)
        current_direction = 4
    else:
        player_idle_animation(current_direction)
    pygame.display.update()
    clock.tick(75)