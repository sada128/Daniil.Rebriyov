import pygame
import random
import sys
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1200, 857))
pygame.display.set_caption('SpishiBisrto')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
updatee = True
font = pygame.font.Font('Rusted Sabbath.ttf', 110)
black = (8, 7, 7)
bg = pygame.image.load('bg.png')
player_anim_count = 0
player = [
    pygame.image.load('0.gif'),
    pygame.image.load('1.gif'),
    pygame.image.load('2.gif'),
    pygame.image.load('3.gif'),
    pygame.image.load('4.gif'),
    pygame.image.load('5.gif'),
    pygame.image.load('6.gif'),
    pygame.image.load('7.gif'),
    pygame.image.load('8.gif'),
    pygame.image.load('9.gif'),
    pygame.image.load('10.gif'),
    pygame.image.load('11.gif'),
    pygame.image.load('12.gif'),
    pygame.image.load('13.gif'),
    pygame.image.load('14.gif'),
    pygame.image.load('15.gif'),
    pygame.image.load('16.gif'),
    pygame.image.load('17.gif'),
    pygame.image.load('18.gif'),
    pygame.image.load('19.gif'),
    pygame.image.load('20.gif'),
    pygame.image.load('21.gif'),
    pygame.image.load('22.gif'),
    pygame.image.load('23.gif')
]

music_playing = False
teacher_images = [
    pygame.image.load('t1.png'),
    pygame.image.load('t2.png')
]
time_for_t1 = 5000
time_for_t2 = 3500
time_for_random = 10000

current_teacher_image = teacher_images[0] 
last_teacher_change_time = pygame.time.get_ticks()

score = 0  
score_font = pygame.font.Font('Rusted Sabbath.ttf', 40)

while updatee:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            updatee = False
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))  # фон

    keys = pygame.key.get_pressed()  # Логика пробела
    if keys[pygame.K_SPACE]:
        if not music_playing:
            pygame.mixer.music.play(-1)
            music_playing = True
        screen.blit(player[player_anim_count], (480, 300))  # Гифка
        if player_anim_count == 23:
            player_anim_count = 0
        else:
            player_anim_count += 1
        score += 1  
    else:
        if music_playing:
            pygame.mixer.music.stop()
            music_playing = False
        screen.blit(player[0], (480, 300))# первый кадр

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_teacher_change_time

    if elapsed_time > time_for_random:
        current_teacher_image = random.choice(teacher_images)
        last_teacher_change_time = current_time
    elif elapsed_time > time_for_t2:
        current_teacher_image = teacher_images[1]
        if music_playing:
            pygame.mixer.music.stop()
            music_playing = False
            game_over_text = font.render("Game Over", 1, black)
            screen.blit(game_over_text, (400, 400))
            score_text = score_font.render(f"Score: {score}", 1, black)
            screen.blit(score_text, (500, 300))
            pygame.mixer.music.load('kitay.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            pygame.display.update()
            pygame.time.delay(6000)  # Пауза 
            updatee = False
            pygame.quit()
            sys.exit()

    if current_teacher_image == teacher_images[0]:
        screen.blit(current_teacher_image, (280, 230))  # Для t1 (280, 230))
    elif current_teacher_image == teacher_images[1]:
        screen.blit(current_teacher_image, (280, 90))  

    text = font.render("Press SPACE while he doesn't see it", 1, black)  # ТЕКСТ
    screen.blit(text, (150, 20))

    score_text = score_font.render(f"Score: {score}", 1, black)
    screen.blit(score_text, (20, 20))

    pygame.display.update()

    clock.tick(25)