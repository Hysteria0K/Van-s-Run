import pygame, sys, time, random
from pygame.locals import *


# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()
FPS = 100

WINDOWWIDTH = 960
WINDOWHEIGHT = 540

# Set up the window.
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 0)
pygame.display.set_caption('Rect object')

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MOVESPEED = 4
MOVE2SPEED = 40
MOBSPEED = 3

SCORE = 0

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def drawText_WHITE(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

Font = pygame.font.Font('comic.ttf', 50)
start_font = pygame.font.SysFont(None, 80)

#sound
button_sound = pygame.mixer.Sound('button.wav')
Scream = pygame.mixer.Sound('Scream.wav')
Die_Scream = pygame.mixer.Sound('Die_Scream.wav')
sword = pygame.mixer.Sound('sword.wav')
mynameisvan = pygame.mixer.Sound('mynameisvan.wav')
dungeon = pygame.mixer.Sound('dungeon.wav')
jump_sound = pygame.mixer.Sound('jump.wav')
deepdarkfantasy = pygame.mixer.Sound('deepdarkfantasy.wav')
hahaha = pygame.mixer.Sound('hahaha.wav')
chokchokhagae = pygame.mixer.Sound('chokchokhagae.wav')
chok1 = pygame.mixer.Sound('chok1.wav')
chok2 = pygame.mixer.Sound('chok2.wav')
fight = pygame.mixer.Sound('fight.wav')

#title image
title = pygame.Rect(0, 0, 960, 540)
titleImage = pygame.image.load('title_img.jpg')
titleStretchedImage = pygame.transform.scale(titleImage, (960, 540))

start = pygame.Rect(30, 180, 240, 120)
startImage = pygame.image.load('start.png')
startStretchedImage = pygame.transform.scale(startImage, (240, 120))

start_hover = pygame.Rect(30, 180, 240, 120)
start_hoverImage = pygame.image.load('start_hover.png')
start_hoverStretchedImage = pygame.transform.scale(start_hoverImage, (240, 120))

Exit = pygame.Rect(35, 300, 180, 124)
ExitImage = pygame.image.load('exit.png')
ExitStretchedImage = pygame.transform.scale(ExitImage, (180, 124))

Exit_hover = pygame.Rect(35, 300, 180, 124)
Exit_hoverImage = pygame.image.load('exit_hover.png')
Exit_hoverStretchedImage = pygame.transform.scale(Exit_hoverImage, (180, 124))

#Tutorial
tutorial = pygame.Rect(0, 0, 960, 540)
tutorialImage = pygame.image.load('Tutorial.png')
tutorialStretchedImage = pygame.transform.scale(tutorialImage, (960, 540))
button = pygame.Rect(700, 270, 450, 450)
buttonImage = pygame.image.load('button.png')
buttonStretchedImage = pygame.transform.scale(buttonImage, (450, 450))

tutorial_count = 0
subcount = 0
subcount2 = 0

#Tutorial_2
tutorial2 = pygame.Rect(200, 150, 560, 250)
tutorial2Image = pygame.image.load('letter.png')
tutorial2StretchedImage = pygame.transform.scale(tutorial2Image, (560, 250))
#stage1_start

#Game
pause_count = 0

background_1 = pygame.Rect(0, 0, 960, 540)
background_1Image = pygame.image.load('background.png')
background_1StretchedImage = pygame.transform.scale(background_1Image, (960, 540))
background_2 = pygame.Rect(960, 0, 960, 540)
background_2Image = pygame.image.load('background.png')
background_2StretchedImage = pygame.transform.scale(background_2Image, (960, 540))

background_call = pygame.Rect(-1000, 0, 40, 20)

player = pygame.Rect(100, 331, 80, 140)
player2 = pygame.Rect(100, 331, 80, 140)
player3 = pygame.Rect(100, 331, 100, 140)
playerImage = pygame.image.load('van1.png')
player2Image = pygame.image.load('panty1.png')
player3Image = pygame.image.load('panty_run.png')
playerStretchedImage = pygame.transform.scale(playerImage, (80, 140))
player2StretchedImage = pygame.transform.scale(player2Image, (80, 140))
player3StretchedImage = pygame.transform.scale(player3Image, (100, 140))

player_atk = pygame.Rect(100, 331, 100, 140)
player_atkImage = pygame.image.load('van2.png')
player_atkStretchedImage = pygame.transform.scale(player_atkImage, (100, 140))
player2_atk = pygame.Rect(100, 331, 100, 140)
player2_atkImage = pygame.image.load('panty2.png')
player2_atkStretchedImage = pygame.transform.scale(player2_atkImage, (100, 140))

atk = pygame.Rect(180, 331, 100, 140)
atkImage = pygame.image.load('atk_effect.png')
atkStretchedImage = pygame.transform.scale(atkImage, (100, 140))

bottom = pygame.Rect(100, 470, 128, 72)
bottomImage = pygame.image.load('타이틀.jpg')
bottomStretchedImage = pygame.transform.scale(bottomImage, (128, 72))

jump = pygame.Rect(100, 100, 128, 72)
jumpImage = pygame.image.load('타이틀.jpg')
jumpStretchedImage = pygame.transform.scale(jumpImage, (128, 72))

bar_x = 0
border = pygame.Rect(195, 25, 570, 40)
flag = pygame.Rect(706, -37, 300, 300)
flagImage = pygame.image.load('flag.png')
flagStretchedImage = pygame.transform.scale(flagImage, (200, 200))

#game_mob
bee1 = pygame.Rect(900, 200, 200, 200)
bee1Image = pygame.image.load('bee1.png')
bee1StretchedImage = pygame.transform.scale(bee1Image, (200, 200))
bee2 = pygame.Rect(900, 200, 200, 200)
bee2Image = pygame.image.load('bee2.png')
bee2StretchedImage = pygame.transform.scale(bee2Image, (200, 200))

bee = 2 #default = 2
bee_count = 0

gob1 = pygame.Rect(400, 322, 250, 250)
gob1Image = pygame.image.load('goblin1.png')
gob1StretchedImage = pygame.transform.scale(gob1Image, (250, 250))
gob2 = pygame.Rect(400, 322, 250, 250)
gob2Image = pygame.image.load('goblin2.png')
gob2StretchedImage = pygame.transform.scale(gob2Image, (250, 250))

gob = 2
gob_count = 0

spike = pygame.Rect(600, 345, 125, 125)
spikeImage = pygame.image.load('spike.png')
spikeStretchedImage = pygame.transform.scale(spikeImage, (125, 125))

spike_ = 2

#boss
boss1 = pygame.Rect(650, 225, 450, 450)
boss1Image = pygame.image.load('boss1.png')
boss1StretchedImage = pygame.transform.scale(boss1Image, (450, 450))
boss2 = pygame.Rect(650, 225, 450, 450)
boss2Image = pygame.image.load('boss2.png')
boss2StretchedImage = pygame.transform.scale(boss2Image, (450, 450))

#bullet
bullet1 = pygame.Rect(482, 312, 200, 150)
bullet1Image = pygame.image.load('bullet.png')
bullet1StretchedImage = pygame.transform.scale(bullet1Image, (200, 150))

bullet_1 = 2
bullet_2 = 2

bullet_call = 0

bullet2 = pygame.Rect(472, 212, 200, 150)
bullet2Image = pygame.image.load('bullet.png')
bullet2StretchedImage = pygame.transform.scale(bullet2Image, (200, 150))

bullet1_par = pygame.Rect(140, 312, 200, 150)
bullet1_parImage = pygame.image.load('bullet_turn.png')
bullet1_parStretchedImage = pygame.transform.scale(bullet1_parImage, (200, 150))

bullet2_par = pygame.Rect(140, 212, 200, 150)
bullet2_parImage = pygame.image.load('bullet_turn.png')
bullet2_parStretchedImage = pygame.transform.scale(bullet2_parImage, (200, 150))

#hit box
van_hit1 = pygame.Rect(110, 412, 34, 60)
van_hit2 = pygame.Rect(110, 352, 68, 68)

bee_hit = pygame.Rect(930, 200, 100, 120)
gob_hit = pygame.Rect(485, 370, 60, 100)
spike_hit = pygame.Rect(640, 450, 37, 25)

hit_call = pygame.Rect(-200, 0, 100, 540)

boss_hit = pygame.Rect(760, 225, 40, 240)
bullet1_hit = pygame.Rect(518, 356, 80, 7)
bullet2_hit = pygame.Rect(508, 260, 80, 7)
bullet1_par_hit = pygame.Rect(170, 356, 80, 7)
bullet2_par_hit = pygame.Rect(170, 260, 80, 7)

bullet1_par_check = 0
bullet2_par_check = 0

boss_hit_check = 0
hit_check = 0
#game_over
gameover_1 = pygame.Rect(0, 0, 960, 540)
gameover_1Image = pygame.image.load('youdied.png')
gameover_1StretchedImage = pygame.transform.scale(gameover_1Image, (960, 540))
gameover_2 = pygame.Rect(0, 0, 960, 540)
gameover_2Image = pygame.image.load('youdied2.png')
gameover_2StretchedImage = pygame.transform.scale(gameover_2Image, (960, 540))

#boss_clear
kill_cut = pygame.Rect(0, 0, 960, 540)
kill_cutImage = pygame.image.load('kill_cut.png')
kill_cutStretchedImage = pygame.transform.scale(kill_cutImage, (960, 540))

life = 3
Move_f = 1
attack = 0
atk_count = 0
gravity = 1
up = 5
jump_check = 0
game_over_check = 0

mob_spawn_count = 1

pantycount = 0

tuto_2 = 0
tuto_2_4 = 0
tuto_2_5 = 0
tuto_2_6 = 0
tuto_2_6_1 = 0

enter_check = 0
gob_check = 0
bee_check = 0
spike_check = 0

# Draw the white background onto the surface.
windowSurface.fill(WHITE)

# Set up keyboard variables.

moveRight = False
moveUp = False
ENTER = False
pause = False

#Game Set
Title = True
Tutorial = False
Tutorial_2 = False
Tuto_2_reset = False
stage1_start = False
Game = False
Stage1_clear = False
Game_over = False
Boss_start = False
Boss_stage = False
Boss_clear_scene = False
Boss_clear = False
Reset = False

#Music
pygame.mixer.music.load('Opening.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

# Run the game loop.
# Intro Loop.
while True:
    while (Title):
        windowSurface.blit(titleStretchedImage, title)
        windowSurface.blit(startStretchedImage, start)
        windowSurface.blit(ExitStretchedImage, Exit)
    
        if start.collidepoint(pygame.mouse.get_pos()):
            windowSurface.blit(start_hoverStretchedImage, start_hover)
        
        if Exit.collidepoint(pygame.mouse.get_pos()):
            windowSurface.blit(Exit_hoverStretchedImage, Exit_hover)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.collidepoint(pygame.mouse.get_pos()):
                    button_sound.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('tutorial_bgm.mp3')
                    pygame.mixer.music.set_volume(0.15)
                    pygame.mixer.music.play()
                    Title = False
                    Tutorial = True
                if Exit.collidepoint(pygame.mouse.get_pos()):
                    button_sound.play()
                    time.sleep(0.5)
                    pygame.quit()
                    sys.exit()
    
        pygame.display.update()
        mainClock.tick(FPS)

    while (Tutorial):
        windowSurface.blit(tutorialStretchedImage, tutorial)
        windowSurface.blit(buttonStretchedImage, button)
        
        if tutorial_count == 0:
            drawText('Hi, My name is Van.', Font, windowSurface, 400, 230)
            if subcount == 0:
                mynameisvan.play()
                subcount += 1
        if tutorial_count == 1:
            drawText('I want to be a ', Font, windowSurface, 400, 230)
            drawText('Dungeon Master.', Font, windowSurface, 400, 300)
            if subcount2 == 0:
                dungeon.play()
                subcount2 += 1
        if tutorial_count == 2:
            drawText("Let's go!", Font, windowSurface, 400, 230)
        if tutorial_count == 3:
            pygame.mixer.music.stop()
            Tutorial = False
            Tutorial_2 = True
            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(pygame.mouse.get_pos()):
                    button_sound.play()
                    tutorial_count += 1

        pygame.display.update()
        mainClock.tick(FPS)
    
    while (Tutorial_2):
        bar = pygame.Rect(200, 30, bar_x, 30)
        windowSurface.blit(background_1StretchedImage, background_1)
        windowSurface.blit(background_2StretchedImage, background_2)
        pygame.draw.rect(windowSurface, WHITE, border)
        pygame.draw.rect(windowSurface, RED, bar)
        windowSurface.blit(flagStretchedImage, flag)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                # Change the keyboard variables.
                if event.key == K_RIGHT: #tuto_2 = 0
                    moveLeft = False
                    moveRight = True
                    if tuto_2 == 0:
                        tuto_2 += 1 #next bar_check
                if event.key == K_SPACE:
                    tuto_2 = 10
                if event.key == K_x:
                    if tuto_2 >= 2:
                        moveDown = False
                        moveUp = True
                        if tuto_2 == 2:
                            tuto_2 += 1 #next atk
                if tuto_2 >= 3:
                    if event.key == K_z:
                        attack = 1
                        if tuto_2 == 3:
                            tuto_2 += 1 #next gob_atk
                if event.key == K_RETURN:
                    if enter_check == 0:
                        ENTER = True
                        enter_check = 1
                      
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_x:
                    moveUp = False
                if event.key == K_z:
                    attack = 0
                    atk_count = 0
                if event.key == K_RETURN:
                    ENTER = False
                    enter_check = 0
                    
                    
        if tuto_2 == 4 and tuto_2_4 == 0:
            tuto_2_4 = 1
            gob = 0
        
        if tuto_2 == 5 and tuto_2_5 == 0:
            tuto_2_5 = 1
            bee = 0
        
        if tuto_2 == 6 or tuto_2 == 7:
            if tuto_2_6 == 0:
                tuto_2_6 = 1
                spike_ = 0
                    
        if moveRight:
            background_1.right -= MOVESPEED * Move_f
            background_2.right -= MOVESPEED * Move_f
            if tuto_2 == 1:
                bar_x += 0.3 #tuto_2 = 1
                if bar_x >= 50:
                    if tuto_2 == 1:
                        tuto_2 += 1 #next = jump
            if bee == 0:
                if bee1.right >= 380:
                    bee1.right -= MOVESPEED
                    bee2.right -= MOVESPEED
                    bee_hit.right -= MOVESPEED
                else:
                    bee_check = 1
                
            if gob == 0:
                if gob1.right >= 380:
                    gob1.right -= MOVESPEED
                    gob2.right -= MOVESPEED
                    gob_hit.right -= MOVESPEED
                else:
                    gob_check = 1
            
            if spike_ == 0:
                if spike.right >= 250 and tuto_2 == 6:
                    spike.right -= MOVESPEED
                    spike_hit.right -= MOVESPEED
                else:
                    spike_check = 1
                if spike.right <= 250 and tuto_2 == 6:
                    if not player.colliderect(bottom) and not player_atk.colliderect(bottom):
                        if moveRight:
                            spike.right -= MOVESPEED
                            spike_hit.right -= MOVESPEED
                            tuto_2 += 1
                            spike_check = 0
                if tuto_2 == 7:
                    spike.right -= MOVESPEED
                    spike_hit.right -= MOVESPEED
                        
        #Mob_move
        if bee == 0:
            if bee1.right >= 380:
                bee1.right -= MOBSPEED
                bee2.right -= MOBSPEED
                bee_hit.right -= MOBSPEED
        if gob == 0:
            if gob1.right >= 380:
                gob1.right -= MOBSPEED
                gob2.right -= MOBSPEED
                gob_hit.right -= MOBSPEED
                        
        if not player.colliderect(bottom) and not player_atk.colliderect(bottom):
            player.top += MOVESPEED * gravity
            player_atk.top += MOVESPEED * gravity
            player2.top += MOVESPEED * gravity
            player2_atk.top += MOVESPEED * gravity
            player3.top += MOVESPEED * gravity
            van_hit1.top += MOVESPEED * gravity
            van_hit2.top += MOVESPEED * gravity
            atk.top += MOVESPEED * gravity
            gravity += 0.1
            
        if player.colliderect(bottom) or player_atk.colliderect(bottom):
            player.top = 331
            player_atk.top = 331
            player2.top = 331
            player2_atk.top = 331
            player3.top = 331
            van_hit1.top = 412
            van_hit2.top = 352
            atk.top = 331
            gravity = 1
            jump_sound_check = 0
            
            if moveUp and player.top > 0:
                jump_check = 1
            if moveUp and player2.top > 0:
                jump_check = 1
        if jump_check == 1:
            if jump_sound_check == 0:
                jump_sound.play()
                jump_sound_check += 1
            player.top -= MOVESPEED * up
            player_atk.top -= MOVESPEED * up
            player2.top -= MOVESPEED * up
            player2_atk.top -= MOVESPEED * up
            player3.top -= MOVESPEED * up
            van_hit1.top -= MOVESPEED * up
            van_hit2.top -= MOVESPEED * up
            atk.top -= MOVESPEED * up
            up -= 0.01
            if player.colliderect(jump) or player_atk.colliderect(jump):
                jump_check = 0
                up = 5
        
        if life == 3:
            if attack == 0:
                windowSurface.blit(playerStretchedImage, player)
            if tuto_2 >= 2:
                if attack == 1:
                    if atk_count == 0:
                        sword.play()
                        windowSurface.blit(atkStretchedImage, atk)
                        atk_count = 1
                    windowSurface.blit(player_atkStretchedImage, player_atk)
                
        if life == 2:
            if attack == 0:
                windowSurface.blit(player2StretchedImage, player2)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player2_atkStretchedImage, player2_atk)
        
        if life == 1:
            windowSurface.blit(player3StretchedImage, player3)
            MOVESPEED = 8
            if pantycount == 0:
                jump.top -= 80
                pantycount = 1
            
        if background_1.colliderect(background_call):
            background_1.right += 1920
        
        if background_2.colliderect(background_call):
            background_2.right += 1920
            
        if spike_hit.colliderect(hit_call):
            spike_ = 2
        
        #mob
        if bee == 0:  #6
            windowSurface.blit(bee1StretchedImage, bee1)
        if gob == 0: #4
            windowSurface.blit(gob1StretchedImage, gob1)
        if spike_ == 0: #5
            windowSurface.blit(spikeStretchedImage, spike)
            
        if atk.colliderect(bee_hit) and atk_count == 1:
            hit_check = 1
            bee1.right += MOBSPEED
            bee2.right += MOBSPEED
            bee_hit.right += MOBSPEED
            bee_check = 2
            
            if moveRight:
                bee1.right += MOVESPEED
                bee2.right += MOVESPEED
                bee_hit.right += MOVESPEED
            bee = 1
            
        if bee == 1:
            windowSurface.blit(bee2StretchedImage, bee2)
            
            bee_count += 1
            
            if bee_count >= 50:
                bee = 2
                
        if bee == 2:
            bee1.right += 1200
            bee2.right += 1200
            bee_hit.right += 1200
            hit_check = 0
            mob_spawn_count = 1
            
            bee = 3
            if tuto_2 == 5:
                tuto_2 += 1
                bee_check = 0
        #mob_atk
        if atk.colliderect(gob_hit) and atk_count == 1:
            hit_check = 1
            gob1.right += MOBSPEED
            gob2.right += MOBSPEED
            gob_hit.right += MOBSPEED
            gob_check = 2
            
            if moveRight:
                gob1.right += MOVESPEED
                gob2.right += MOVESPEED
                gob_hit.right += MOVESPEED
            gob = 1
            
        if gob == 1:
            windowSurface.blit(gob2StretchedImage, gob2)
            
            gob_count += 1
            
            if gob_count >= 50:
                gob = 2

        if gob == 2:
            gob1.right += 1200
            gob2.right += 1200
            gob_hit.right += 1200
            hit_check = 0
            mob_spawn_count = 1
            
            gob = 3
            if tuto_2 == 4:
                tuto_2 += 1
                gob_check = 0
        
        if spike_ == 2:
            spike.right += 1200
            spike_hit.right += 1200
            hit_check = 0
            mob_spawn_count = 1
            
            spike_ = 3
            if tuto_2 == 7:
                tuto_2 += 1
                
        windowSurface.blit(tutorial2StretchedImage, tutorial2)
        
        if tuto_2 == 0:
            drawText_WHITE("Push 'Right' key to run", Font, windowSurface, 210, 235)
            
        if tuto_2 == 1:
            drawText_WHITE("Check the upper bar" , Font, windowSurface, 240, 200)
            drawText_WHITE("when you run", Font, windowSurface, 330, 280)
        
        if tuto_2 == 2:
            drawText_WHITE("Push 'X' key to jump", Font, windowSurface, 242, 235)
        
        if tuto_2 == 3:
            drawText_WHITE("Push 'Z' key to attack", Font, windowSurface, 218, 235)
        
        if tuto_2 == 4 and gob_check == 0:
            drawText_WHITE("Run!", Font, windowSurface, 440, 235)
        if tuto_2 == 4 and gob_check == 1:
            drawText_WHITE("Attack the goblin!", Font, windowSurface, 270, 235)
        if tuto_2 == 4 and gob_check == 2:
            drawText_WHITE("Good Job!", Font, windowSurface, 370, 235)

        if tuto_2 == 5 and bee_check == 0:
            drawText_WHITE("Run!", Font, windowSurface, 440, 235)
        if tuto_2 == 5 and bee_check == 1:
            drawText_WHITE("Jump and attack", Font, windowSurface, 290, 200)
            drawText_WHITE("the wasp!", Font, windowSurface, 370, 280)
        if tuto_2 == 5 and bee_check == 2:
            drawText_WHITE("Good Job!", Font, windowSurface, 370, 235)
        
        if tuto_2 == 6 and spike_check == 0:
            drawText_WHITE("Run!", Font, windowSurface, 440, 235)
        if tuto_2 == 6 and spike_check == 1:
            drawText_WHITE("Run and jump to", Font, windowSurface, 290, 200)
            drawText_WHITE("avoid the spike!", Font, windowSurface, 290, 280)
        if tuto_2 == 7:
            drawText_WHITE("Good Job!", Font, windowSurface, 370, 235)
                         
        if tuto_2 == 8:
            drawText_WHITE("Van has 2 equips.", Font, windowSurface, 290, 200)
            drawText_WHITE("Push 'Enter' to next", Font, windowSurface, 240, 280)
            if ENTER == True:
                tuto_2 += 1
            ENTER = False
        
        if tuto_2 == 9:
            life = 2
            drawText_WHITE("He will lost them if", Font, windowSurface, 250, 160)
            drawText_WHITE("he hitted by monsters", Font, windowSurface, 220, 240)
            drawText_WHITE("Push 'Enter' to next", Font, windowSurface, 240, 320)
            if ENTER == True:
                tuto_2 += 1
            ENTER = False
            
        if tuto_2 == 10:
            life = 1
            drawText_WHITE("If he lost them all,", Font, windowSurface, 270, 160)
            drawText_WHITE("he can move faster.", Font, windowSurface, 265, 240)
            drawText_WHITE("Push 'Enter' to start", Font, windowSurface, 240, 320)
            if ENTER == True:
                Tutorial_2 = False
                Tuto_2_reset = True
            
        pygame.display.update()
        mainClock.tick(FPS)
    
    while (Tuto_2_reset):
        if life <= 1:
            jump.top += 80
        player.top = 331
        player_atk.top = 331
        player2.top = 331
        player2_atk.top = 331
        player3.top = 331
        van_hit1.top = 412
        van_hit2.top = 352
        atk.top = 331
        MOVESPEED = 4
        life = 3
        bar_x = 0
        Move_f = 1
        attack = 0
        atk_count = 0
        gravity = 1
        up = 5
        jump_check = 0
        game_over_check = 0
        mob_spawn_count = 1
        bee = 2
        bee_count = 0
        gob = 2
        gob_count = 0
        spike_ = 2
        pantycount = 0
        tuto_2 = 0
        tuto_2_4 = 0
        tuto_2_5 = 0
        tuto_2_6 = 0
        tuto_2_6_1 = 0
        enter_check = 0
        gob_check = 0
        bee_check = 0
        spike_check = 0
        bullet_1 = 2
        bullet_2 = 2
        bullet_call = 0
        boss_hit_check = 0
        boss_hit_count = 0
        moveRight = False
        moveUp = False
        ENTER = False
        pause = False
        Tuto_2_reset = False
        stage1_start = True
        
    while (stage1_start):
        windowSurface.fill(BLACK)
        drawText_WHITE('Stage 1', start_font, windowSurface, 380, 200)
        drawText_WHITE('Start!', start_font, windowSurface, 400, 300)
        
        pygame.display.update()
        mainClock.tick(FPS)
        
        deepdarkfantasy.play()
        time.sleep(2)
        pygame.mixer.music.load('BGM.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
        time.sleep(1)
        stage1_start = False
        Game = True
                   
    while (Game):
        windowSurface.blit(background_1StretchedImage, background_1)
        windowSurface.blit(background_2StretchedImage, background_2)
        if pause == True:
            while(pause):
                if pause_count == 0:
                    windowSurface.blit(tutorial2StretchedImage, tutorial2)
                    drawText_WHITE("Pause", Font, windowSurface, 430, 235)
                    pause_count = 1
                    
                pygame.display.update()
                mainClock.tick(FPS)
                time.sleep(0.5)
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            pause = False
                            pause_count = 0
        bar = pygame.Rect(200, 30, bar_x, 30)
        
        if bar_x >= 565:
            Game = False
            Stage1_clear = True
        # Check for events.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                # Change the keyboard variables.
                if event.key == K_RIGHT:
                    moveLeft = False
                    moveRight = True
                if event.key == K_x:
                    moveDown = False
                    moveUp = True
                if event.key == K_z:
                    attack = 1
                if event.key == K_SPACE:
                    pause = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_x:
                    moveUp = False
                if event.key == K_z:
                    attack = 0
                    atk_count = 0
                    
        if hit_check == 0 and mob_spawn_count == 1:
            mob_spawn = random.randint(0, 2)
            if mob_spawn == 0:
                bee = 0
            if mob_spawn == 1:
                gob = 0
            if mob_spawn == 2:
                spike_ = 0
            mob_spawn_count = 0
        
        #mob
        if bee == 0:  #1
            windowSurface.blit(bee1StretchedImage, bee1)
        if gob == 0:
            windowSurface.blit(gob1StretchedImage, gob1)
        if spike_ == 0:
            windowSurface.blit(spikeStretchedImage, spike)
    
        # Move the player.
        #Jump
        if not player.colliderect(bottom) and not player_atk.colliderect(bottom):
            player.top += MOVESPEED * gravity
            player_atk.top += MOVESPEED * gravity
            player2.top += MOVESPEED * gravity
            player2_atk.top += MOVESPEED * gravity
            player3.top += MOVESPEED * gravity
            van_hit1.top += MOVESPEED * gravity
            van_hit2.top += MOVESPEED * gravity
            atk.top += MOVESPEED * gravity
            gravity += 0.1
            
        if player.colliderect(bottom) or player_atk.colliderect(bottom):
            player.top = 331
            player_atk.top = 331
            player2.top = 331
            player2_atk.top = 331
            player3.top = 331
            van_hit1.top = 412
            van_hit2.top = 352
            atk.top = 331
            gravity = 1
            jump_sound_check = 0
            
            if moveUp and player.top > 0:
                jump_check = 1
            if moveUp and player2.top > 0:
                jump_check = 1
        if jump_check == 1:
            if jump_sound_check == 0:
                jump_sound.play()
                jump_sound_check += 1
            player.top -= MOVESPEED * up
            player_atk.top -= MOVESPEED * up
            player2.top -= MOVESPEED * up
            player2_atk.top -= MOVESPEED * up
            player3.top -= MOVESPEED * up
            van_hit1.top -= MOVESPEED * up
            van_hit2.top -= MOVESPEED * up
            atk.top -= MOVESPEED * up
            up -= 0.01
            if player.colliderect(jump) or player_atk.colliderect(jump):
                jump_check = 0
                up = 5
        if moveRight:
            background_1.right -= MOVESPEED * Move_f
            background_2.right -= MOVESPEED * Move_f
            if life == 1:
                bar_x += 0.6
            else:
                bar_x += 0.3
            
            if bee == 0:
                bee1.right -= MOVESPEED
                bee2.right -= MOVESPEED
                bee_hit.right -= MOVESPEED
            
            if gob == 0:
                gob1.right -= MOVESPEED
                gob2.right -= MOVESPEED
                gob_hit.right -= MOVESPEED
            
            if spike_ == 0:
                spike.right -= MOVESPEED
                spike_hit.right -= MOVESPEED
      
        #Mob_move
        if bee == 0:  
            bee1.right -= MOBSPEED
            bee2.right -= MOBSPEED
            bee_hit.right -= MOBSPEED
        if gob == 0:
            gob1.right -= MOBSPEED
            gob2.right -= MOBSPEED
            gob_hit.right -= MOBSPEED
        
        # Draw the block onto the surface.
        if life == 3:
            if attack == 0:
                windowSurface.blit(playerStretchedImage, player)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player_atkStretchedImage, player_atk)
                
        if life == 2:
            if attack == 0:
                windowSurface.blit(player2StretchedImage, player2)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player2_atkStretchedImage, player2_atk)
        
        if life == 1:
            windowSurface.blit(player3StretchedImage, player3)
            MOVESPEED = 8
            if pantycount == 0:
                jump.top -= 80
                pantycount = 1
            

        if background_1.colliderect(background_call):
            background_1.right += 1920
        
        if background_2.colliderect(background_call):
            background_2.right += 1920
        
        if van_hit1.colliderect(bee_hit) or van_hit2.colliderect(bee_hit):
            if hit_check == 0:
                if life != 1:
                    Scream.play()
                else:
                    Die_Scream.play()
                life -= 1
                hit_check = 1
        if bee_hit.colliderect(hit_call):
            bee = 2
        
        if van_hit1.colliderect(gob_hit) or van_hit2.colliderect(gob_hit):
            if hit_check == 0:
                if life != 1:
                    Scream.play()
                else:
                    Die_Scream.play()
                life -= 1
                hit_check = 1
        if gob_hit.colliderect(hit_call):
            gob = 2
            
        if van_hit1.colliderect(spike_hit) or van_hit2.colliderect(spike_hit):
            if hit_check == 0:
                if life != 1:
                    Scream.play()
                else:
                    Die_Scream.play()
                life -= 1
                hit_check = 1
        if spike_hit.colliderect(hit_call):
            spike_ = 2
            
        if atk.colliderect(bee_hit) and atk_count == 1:
            hit_check = 1
            bee1.right += MOBSPEED
            bee2.right += MOBSPEED
            bee_hit.right += MOBSPEED
            
            if moveRight:
                bee1.right += MOVESPEED
                bee2.right += MOVESPEED
                bee_hit.right += MOVESPEED
            bee = 1
            
        if bee == 1:
            windowSurface.blit(bee2StretchedImage, bee2)
            
            bee_count += 1
            
            if bee_count >= 50:
                bee = 2
                
        if bee == 2:
            bee1.right += 1200
            bee2.right += 1200
            bee_hit.right += 1200
            hit_check = 0
            mob_spawn_count = 1
            
            bee = 3
        
        if atk.colliderect(gob_hit) and atk_count == 1:
            hit_check = 1
            gob1.right += MOBSPEED
            gob2.right += MOBSPEED
            gob_hit.right += MOBSPEED
            
            if moveRight:
                gob1.right += MOVESPEED
                gob2.right += MOVESPEED
                gob_hit.right += MOVESPEED
            gob = 1
            
        if gob == 1:
            windowSurface.blit(gob2StretchedImage, gob2)
            
            gob_count += 1
            
            if gob_count >= 50:
                gob = 2
        
        if gob == 2:
            gob1.right += 1200
            gob2.right += 1200
            gob_hit.right += 1200
            hit_check = 0
            mob_spawn_count = 1
            
            gob = 3
        
        if spike_ == 2:
            spike.right += 1200
            spike_hit.right += 1200
            hit_check = 0
            mob_spawn_count = 1
            
            spike_ = 3
            
        pygame.draw.rect(windowSurface, WHITE, border)
        pygame.draw.rect(windowSurface, RED, bar)
        windowSurface.blit(flagStretchedImage, flag)
        
        #hitbox
        '''pygame.draw.rect(windowSurface, BLACK, van_hit1)
        pygame.draw.rect(windowSurface, BLACK, van_hit2)
        pygame.draw.rect(windowSurface, BLACK, bee_hit)
        pygame.draw.rect(windowSurface, BLACK, gob_hit)
        pygame.draw.rect(windowSurface, BLACK, spike_hit)'''

        if life <= 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Die_BGM.mp3')
            pygame.mixer.music.play()
            Game = False
            Game_over = True
        
        pygame.display.update()
        mainClock.tick(FPS)
        
    while (Stage1_clear):
        pygame.mixer.music.stop()
        windowSurface.fill(BLACK)
        drawText_WHITE('Stage 1', start_font, windowSurface, 380, 200)
        drawText_WHITE('Clear!', start_font, windowSurface, 400, 300)
        
        pygame.display.update()
        mainClock.tick(FPS)

        time.sleep(2)
        
        life = 3 
        Stage1_clear = False
        Boss_start = True

    while (Boss_start):
        hahaha.play()
        windowSurface.fill(BLACK)
        drawText_WHITE('Boss battle', start_font, windowSurface, 330, 200)
        drawText_WHITE('Start!', start_font, windowSurface, 400, 300)

        pygame.display.update()
        mainClock.tick(FPS)
        
        bar_x = 545
        
        time.sleep(6)
        chokchokhagae.play()
        #촉촉이 히히히히히힣히 사운드 추가
        pygame.mixer.music.stop()
        pygame.mixer.music.load('boss_bgm.mp3')
        pygame.mixer.music.play(-1)
        Boss_start = False
        Boss_stage = True

    while (Boss_stage):
        windowSurface.blit(background_1StretchedImage, background_1)
        windowSurface.blit(background_2StretchedImage, background_2)
        bar = pygame.Rect(200, 30, bar_x, 30)
        
        if bar_x <= 0:
            pygame.mixer.music.stop()
            budul = 0
            Boss_stage = False
            Boss_clear_scene = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moveRight = True
                if event.key == K_x:
                    moveDown = False
                    moveUp = True
                if event.key == K_z:
                    attack = 1
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_x:
                    moveUp = False
                if event.key == K_z:
                    attack = 0
                    atk_count = 0
                    
        if bullet_call == 0:
            bullet_select = random.randint(0, 1)
            if bullet_select == 0:
                bullet_1 = 0
                chok1.play()
            if bullet_select == 1:
                bullet_2 = 0
                chok2.play()
            bullet_call = 1
                
        if bullet_1 == 0:
            windowSurface.blit(bullet1StretchedImage, bullet1)
        if bullet_2 == 0:
            windowSurface.blit(bullet2StretchedImage, bullet2)
        
        if boss_hit_check == 0:
            windowSurface.blit(boss1StretchedImage, boss1)
            boss_hit_count = 0
        
        if boss_hit_check == 1:
            windowSurface.blit(boss2StretchedImage, boss2)
            boss_hit_count += 0.1
        
        if boss_hit_count >= 5:
            boss_hit_check = 0
            boss_hit_count = 0
       

        # Move the player.
        #Jump
        if not player.colliderect(bottom) and not player_atk.colliderect(bottom):
            player.top += MOVESPEED * gravity
            player_atk.top += MOVESPEED * gravity
            player2.top += MOVESPEED * gravity
            player2_atk.top += MOVESPEED * gravity
            player3.top += MOVESPEED * gravity
            van_hit1.top += MOVESPEED * gravity
            van_hit2.top += MOVESPEED * gravity
            atk.top += MOVESPEED * gravity
            gravity += 0.1
            
        if player.colliderect(bottom) or player_atk.colliderect(bottom):
            player.top = 331
            player_atk.top = 331
            player2.top = 331
            player2_atk.top = 331
            player3.top = 331
            van_hit1.top = 412
            van_hit2.top = 352
            atk.top = 331
            gravity = 1
            jump_sound_check = 0
            
            if moveUp and player.top > 0:
                jump_check = 1
            if moveUp and player2.top > 0:
                jump_check = 1
        if jump_check == 1:
            if jump_sound_check == 0:
                jump_sound.play()
                jump_sound_check += 1
            player.top -= MOVESPEED * up
            player_atk.top -= MOVESPEED * up
            player2.top -= MOVESPEED * up
            player2_atk.top -= MOVESPEED * up
            player3.top -= MOVESPEED * up
            van_hit1.top -= MOVESPEED * up
            van_hit2.top -= MOVESPEED * up
            atk.top -= MOVESPEED * up
            up -= 0.01
            if player.colliderect(jump) or player_atk.colliderect(jump):
                jump_check = 0
                up = 5
                
        if moveRight:
            background_1.right -= MOVESPEED * Move_f
            background_2.right -= MOVESPEED * Move_f
            bar_x -= 0.3
            if life == 1:
                bar_x -= 0.6

            if bullet_1  == 0:  
                bullet1.right -= MOVESPEED
                bullet1_hit.right -= MOVESPEED
            if bullet_2  == 0:  
                bullet2.right -= MOVESPEED
                bullet2_hit.right -= MOVESPEED
                
            if bullet1_par_check == 1:
                bullet1_par.right += MOVESPEED
                bullet1_par_hit.right += MOVESPEED
                
            if bullet2_par_check == 1:
                bullet2_par.right += MOVESPEED
                bullet2_par_hit.right += MOVESPEED
                
        #bullet_move
        if bullet_1  == 0:  
            bullet1.right -= MOBSPEED * 1.3
            bullet1_hit.right -= MOBSPEED * 1.3
            
        if bullet_2  == 0:  
            bullet2.right -= MOBSPEED * 1.3
            bullet2_hit.right -= MOBSPEED * 1.3

        if bullet1_hit.colliderect(hit_call) or bullet_1 == 2:
            bullet_1 = 1
            bullet1.right += 732
            bullet1_hit.right += 732
            hit_check = 0
            bullet_call = 0

        if bullet2_hit.colliderect(hit_call) or bullet_2 == 2:
            bullet_2 = 1
            bullet2.right += 722
            bullet2_hit.right += 722
            hit_check = 0
            bullet_call = 0

        if van_hit1.colliderect(bullet1_hit) or van_hit2.colliderect(bullet1_hit):
            if hit_check == 0:
                if life != 1:
                    Scream.play()
                else:
                    Die_Scream.play()
                life -= 1
                hit_check = 1
            if bullet1_hit.colliderect(hit_call):
                bullet_1 = 2

        if van_hit1.colliderect(bullet2_hit) or van_hit2.colliderect(bullet2_hit):
            if hit_check == 0:
                if life != 1:
                    Scream.play()
                else:
                    Die_Scream.play()
                life -= 1
                hit_check = 1
            if bullet2_hit.colliderect(hit_call):
                bullet_2 = 2
        
        if bullet1_par_check == 1:
            windowSurface.blit(bullet1_parStretchedImage, bullet1_par)
            bullet1_par.right += MOBSPEED * 2
            bullet1_par_hit.right += MOBSPEED * 2
            
            if bullet1_par_hit.colliderect(boss_hit):
                boss_hit_check = 1
                bar_x -= 10
                bullet1_par.right -= 700
                bullet1_par_hit.right -= 700
                bullet1_par_check = 0
        
        if bullet2_par_check == 1:
            windowSurface.blit(bullet2_parStretchedImage, bullet2_par)
            bullet2_par.right += MOBSPEED * 2
            bullet2_par_hit.right += MOBSPEED * 2
            
            if bullet2_par_hit.colliderect(boss_hit):
                boss_hit_check = 1
                bar_x -= 10
                bullet2_par.right -= 700
                bullet2_par_hit.right -= 700
                bullet2_par_check = 0

                
        if atk.colliderect(bullet1_hit) and atk_count == 1:
            hit_check = 1
            bullet_1 = 2
            bullet1_par_check = 1

        if atk.colliderect(bullet2_hit) and atk_count == 1:
            hit_check = 1
            bullet_2 = 2
            bullet2_par_check = 1

        # Draw the block onto the surface.
        if life == 3:
            if attack == 0:
                windowSurface.blit(playerStretchedImage, player)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player_atkStretchedImage, player_atk)
                
        if life == 2:
            if attack == 0:
                windowSurface.blit(player2StretchedImage, player2)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player2_atkStretchedImage, player2_atk)
        
        if life == 1:
            windowSurface.blit(player3StretchedImage, player3)
            MOVESPEED = 12
            if pantycount == 0:
                jump.top -= 80
                pantycount = 1

        if life <= 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Die_BGM.mp3')
            pygame.mixer.music.play()
            Boss_stage = False
            Game_over = True

        if background_1.colliderect(background_call):
            background_1.right += 1920
        
        if background_2.colliderect(background_call):
            background_2.right += 1920

        pygame.draw.rect(windowSurface, WHITE, border)
        pygame.draw.rect(windowSurface, RED, bar)

        pygame.display.update()
        mainClock.tick(FPS)

    while (Game_over):
        if game_over_check <= 100:
            windowSurface.blit(gameover_1StretchedImage, gameover_1)
            game_over_check += 2
        if game_over_check >= 100:
            windowSurface.blit(gameover_2StretchedImage, gameover_2)
            game_over_check += 2
        if game_over_check >= 200:
            game_over_check = 0
            
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('BGM.mp3')
                    pygame.mixer.music.play()
                    Game_over = False
                    Reset = True
                    
        pygame.display.update()
        mainClock.tick(FPS)
    
    while (Boss_clear_scene):
        windowSurface.blit(background_1StretchedImage, background_1)
        windowSurface.blit(background_2StretchedImage, background_2)
        windowSurface.blit(boss2StretchedImage, boss2)
        
        if life == 3:
            if attack == 0:
                windowSurface.blit(playerStretchedImage, player)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player_atkStretchedImage, player_atk)
                
        if life == 2:
            if attack == 0:
                windowSurface.blit(player2StretchedImage, player2)
            if attack == 1:
                if atk_count == 0:
                    sword.play()
                    windowSurface.blit(atkStretchedImage, atk)
                    atk_count = 1
                windowSurface.blit(player2_atkStretchedImage, player2_atk)
        
        if life == 1:
            windowSurface.blit(player3StretchedImage, player3)
            MOVESPEED = 12
            if pantycount == 0:
                jump.top -= 80
                pantycount = 1
                
        if budul <= 80:
            if budul %2 == 0:
                boss2.right += 50
            else:
                boss2.right -= 50
            budul += 1
            time.sleep(0.003)
                
        pygame.display.update()
        mainClock.tick(FPS)
        
        if budul > 80:
            Boss_clear_scene = False
            Boss_clear = True
        
    while (Boss_clear):
        windowSurface.blit(kill_cutStretchedImage, kill_cut)
        fight.play()
        
        pygame.display.update()
        mainClock.tick(FPS)
        
        time.sleep(2)
        drawText_WHITE('Boss', start_font, windowSurface, 405, 200)
        drawText_WHITE('Clear!', start_font, windowSurface, 400, 300)
        
        pygame.display.update()
        mainClock.tick(FPS)
        
        time.sleep(3)
        
        pygame.mixer.music.load('Opening.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        Boss_clear = False
        Title = True
        
    while (Reset):
        if life <= 1:
            jump.top += 80
        player.top = 331
        player_atk.top = 331
        player2.top = 331
        player2_atk.top = 331
        player3.top = 331
        van_hit1.top = 412
        van_hit2.top = 352
        atk.top = 331
        life = 3
        bar_x = 0
        Move_f = 1
        attack = 0
        atk_count = 0
        gravity = 1
        up = 5
        jump_check = 0
        game_over_check = 0
        mob_spawn_count = 1
        bee = 2
        bee_count = 0
        gob = 2
        gob_count = 0
        spike_ = 2
        pantycount = 0
        tuto_2 = 0
        MOVESPEED = 4
        enter_check = 0
        gob_check = 0
        bee_check = 0
        spike_check = 0
        bullet_1 = 2
        bullet_2 = 2
        bullet_call = 0
        boss_hit_check = 0
        boss_hit_count = 0
        moveRight = False
        moveUp = False
        ENTER = False
        pause = False
        Reset = False
        Game = True
        


    
    
