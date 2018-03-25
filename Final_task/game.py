import pygame
import random
from someone import Player
from platforms import *
#import coin

# Создание окна
WIDTH = 1200
HEIGHT = 600
bg_color = 'darkgreen'
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game')
screen = pygame.Surface((WIDTH, HEIGHT))

hero = Player(30, HEIGHT-60)
left = right = up = False

level= [
    '=-------===-----====--------==----------',
    '-   **               ***       **      -',
    '-   -=-     *        --=       ==      =',
    '=           --     *              *    -',
    '-  **   ***       ==             --  **-',
    '-      =--==         *     ==  *     =--',
    '- *                 --         -       -',
    '--=-   *     =                         -',
    '-   *           =-     *      -=--     -',
    '-   --=-               -    *          =',
    '=      *      =   *         =          -',
    '-*     ---            --=-      --     -',
    '-=       ***     --                    -',
    '-        -=--=      ***     ***        -',
    '-      **           --=    --=-       --',
    '-     --=           **         ***     -',
    '-**             -==---        ---=     -',
    '===       *              ***         -=-',
    '-        --       **     ==--    **    -',
    '---=---------===-------------==------==-',]

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms = []
coin_group = pygame.sprite.Group()
coins = []
x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == '=':
            pl = Platform2(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == '*':
            pl = Coin(x+6, y+7)
            coin_group.add(pl)
            coins.append(pl)
        x += 30
    y += 30
    x = 0


        

#pl = pygame.Surface((30, 30))
#pl.fill(pygame.Color('black'))

# hero create

    
end_game = False
timer = pygame.time.Clock()
while not end_game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            end_game = True

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False



    screen.fill(pygame.Color(bg_color))
    #create_lvl(level1, pl)

    hero.update(left, right, up, platforms)
    sprite_group.draw(screen)
    coin_group.draw(screen)

    window.blit(screen, (0, 0))

    pygame.display.flip()
    timer.tick(50)
    
