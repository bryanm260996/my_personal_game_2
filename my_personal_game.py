#Received serious help from Jackson
import pygame
import sys

from game_parameters import *
from GAME.healthy_food import shakes, yogurts
from GAME.background import draw_background, add_shake, add_enemies, add_yogurt, add_enemies2, add_enemies3,  draw_background2, draw_background3
from GAME.player import Player
from GAME.enemy import enemies, enemies2, enemies3

#initialize pygame
pygame.init()

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('adding a player on the screen')
clock= pygame.time.Clock()

#create a player
player = Player(screen_width/2, screen_height/2)

#initialize score
score= 0

score_font= pygame.font.Font('../assets/fonts/DERSIRA.ttf', 50)
text= score_font.render(f'{score}',True, (255,0,0))
fast_font=pygame.font.Font('../assets/fonts/DERSIRA.ttf', 40)


#load sound effects
eat_sound= pygame.mixer.Sound('../assets/sounds/chomp.wav')
ew_sound=pygame.mixer.Sound('../assets/sounds/MITCH.wav')
emma_sound=pygame.mixer.Sound('../assets/sounds/emma.wav')
lives= 10
running=True
dead = True
active= True
while active:
    background1 = screen.copy()
    draw_background(background1)
    draw_background3(background1)
    screen.blit(background1, (0, 0))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_y:
                active= False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lives = 0
            dead = False
            running=False


    background = screen.copy()
    draw_background(background)
    # draw items
    add_shake(1)
    add_yogurt(1)
    # draw enemies
    add_enemies(1)
    add_enemies2(1)
    add_enemies3(1)
    screen.blit(background, (0, 0))





    while lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lives = 0
                dead = False
                running=False
        #control player with keyboard
            player.stop()

            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.down()
                if event.key == pygame.K_SPACE:
                    player.dissapear()



#DRAW BACKGROUND
    #screen.blit(background, (0, 0))
    #DRAW items
        shakes.update()
        player.update()
        enemies.update()
        yogurts.update()
        enemies2.update()
        enemies3.update()



    #check for player collisions with items

        result=pygame.sprite.spritecollide(player, shakes, True)
    #print(result)
        if result:
        #play sound
            pygame.mixer.Sound.play(eat_sound)
            score += 1
            print(score)
    # draw more  core_powrs
            add_shake(len(result))
            player.image=player.celebratory_image

        result = pygame.sprite.spritecollide(player, yogurts, True)

        if result:  # if it is not empty
        # play sound
            pygame.mixer.Sound.play(eat_sound)
            score += 1
            print(score)
        # draw more  core_powers
            add_yogurt(len(result))
            player.image=player.celebratory_image


        result = pygame.sprite.spritecollide(player, enemies, True)
        if result: #if it is not empty
        #play sound
            pygame.mixer.Sound.play(ew_sound)
            score -= 1
            lives -=1
            print(score)
    # draw more  enemies
            add_enemies(len(result))
            player.image=player.hurt

        result = pygame.sprite.spritecollide(player, enemies2, True)
        if result:
        #play sound
            pygame.mixer.Sound.play(ew_sound)
            score -= 1
            lives -= 1
            print(score)
    # draw more items
            add_enemies2(len(result))
            player.image = player.hurt
        result = pygame.sprite.spritecollide(player, enemies3, True)
        if result:
        #play sound
            pygame.mixer.Sound.play(ew_sound)
            score -= 1
            lives -= 1
            print(score)
    # draw more items
            add_enemies3(len(result))
            player.image = player.hurt

    #check if any items is off the screen
        for shake in shakes:
            if shake.rect.y > 600:
                shakes.remove(shake)
                add_shake(1)

        for yogurt in yogurts:
            if yogurt.rect.y > 600:
                yogurts.remove(yogurt)
                add_yogurt(1)

        for enemy in enemies:
            if enemy.rect.y > 600:
                enemies.remove(enemy)
                add_enemies(1)

        for enemy2 in enemies2:
            if enemy2.rect.y > 600:
                enemies2.remove(enemy2)
                add_enemies2(1)
        for enemy3 in enemies3:
            if enemy3.rect.x < -600:
                enemies3.remove(enemy3)
                add_enemies3(1)


#draw items
        screen.blit(background, (0, 0))
        shakes.draw(screen)
        enemies.draw(screen)
        yogurts.draw(screen)
        enemies2.draw(screen)
        enemies3.draw(screen)


#draw player
        player.draw(screen)
#create a font to give messages while player is playing
        custom_font = pygame.font.Font('../assets/fonts/DERSIRA.ttf', 30)
        custom_font_small= pygame.font.Font('../assets/fonts/DERSIRA.ttf', 25)
    # draw score on screen and make it change color depending on score
        if score <0:
            score=0
            clock.tick(60)


        #elif score < 2:

            #clock.tick(60)
            #text = score_font.render(f'{score}', True, (255, 255, 0))


        elif score <10:
            level= custom_font_small.render('LEVEL 1', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (255, 255, 0))
            clock.tick(65)
        elif score <20:
            level= custom_font_small.render('LEVEL 2', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (255, 255, 0))
            clock.tick(70)
        elif score == 30:
            pygame.mixer.Sound.play(emma_sound)
            clock.tick(75)
            lives=10
        elif score <30:
            level= custom_font_small.render('LEVEL 3', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (0, 255, 0))
            clock.tick(75)
        elif score <40:
            level= custom_font_small.render('LEVEL 4', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (0, 255, 0))
            clock.tick(80)
        elif score == 60:
            pygame.mixer.Sound.play(emma_sound)
            clock.tick(100)
            lives=10
        elif score <50:
            level= custom_font_small.render('LEVEL 5', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (0, 255, 0))
            clock.tick(90)
        elif score <60:
            level= custom_font_small.render('LEVEL 6', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (0, 255, 0))
            clock.tick(100)
        elif score <70:
            level= custom_font_small.render('LEVEL 7', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (0, 255, 0))
            clock.tick(110)
        else:
            level= custom_font_small.render('LEVEL 8', True, (255,0,0))
            screen.blit(level,(680,20))
            text = score_font.render(f'{score}', True, (0, 255, 0))
            clock.tick(120)


# draws the score on the screen
        screen.blit(text, (screen_width/2, tile_size))
# draw the number of lives on top of the screen
        for i in range(lives):
            screen.blit(player.small_celebratory_image, (i*20, 10))

        pygame.display.flip()
    #clock.tick(60)

#CREATE NEW BACKGROUND WHEN GAME OVER
    screen.blit(background, (0, 0))


#SHOW GAME OVER MESSAGE and FINAL SCORE
    draw_background2(background)
    screen.blit(background, (0, 0))
#message = score_font.render('GAME OVER', True, (255,0,0))
#screen.blit(message,(screen_width/2- message.get_width()/2, screen_height/2 - message.get_height()/2))
    score_text= score_font.render(f' Final Score: {score}', True, (255,0,0))
    screen.blit(score_text, (220,340))

#update display

    pygame.display.flip()

#WAIT FOR USER TO EXIT GAME
    dead = True
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_y:
                    lives = 10
                    score=0
                    shakes.empty()
                    yogurts.empty()
                    enemies.empty()
                    enemies2.empty()
                    enemies3.empty()
                    dead = False
                    running=True
pygame.quit()
sys.exit()




