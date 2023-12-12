import pygame 

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 567), ) #flags= pygame.NOFRAME 
pygame.display.set_caption('Lapiti')
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)


bg = pygame.image.load('image/bg.png')

pygame.display.set_icon(icon)
walk_left = [ 
    pygame.image.load('image/left1.png'),
    pygame.image.load('image/left2.png'),
    pygame.image.load('image/left3.png'),
    pygame.image.load('image/left4.png'),
    pygame.image.load('image/left5.png'),
    pygame.image.load('image/left6.png')





]
walk_right = [ 
    pygame.image.load('image/right1.png'),
    pygame.image.load('image/right2.png'),
    pygame.image.load('image/right3.png'),
    pygame.image.load('image/right4.png'),
    pygame.image.load('image/right5.png'),
    pygame.image.load('image/right6.png')
      
]
player_anim_count = 0
bg_x = 0
player_speed = 15
player_x = 375
player_y = 385

is_jump = False
jump_count = 7
bg_sound = pygame.mixer.Sound('image/bg.mp3')
bg_sound.play()


running = True
while running:
    keys = pygame.key.get_pressed()
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1000, 0))
    if keys[pygame.K_LEFT]:
       screen.blit(walk_left[player_anim_count], (player_x,player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x,player_y))

    
    
    if keys[pygame.K_LEFT] and player_x :
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x :
        player_x += player_speed
    
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else: 
        if jump_count >=-7:
           if jump_count > 0:
               player_y -= (jump_count **2)/2
           else:
               player_y += (jump_count **2)/2
           jump_count -=1
        else:
            is_jump = False
            jump_count = 7
    if   player_anim_count ==5:
        player_anim_count = 0
    else:
        player_anim_count += 1    

    bg_x -=1
    if bg_x == -1000:
        bg_x = 0   



    



    pygame.display.update()
    screen.fill((51, 44, 148))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(7)
