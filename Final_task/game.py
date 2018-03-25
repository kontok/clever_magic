import pygame
import random
from someone import Player
from platforms import *
#import coin

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
sound = pygame.mixer.Sound('sounds/start.ogg')


# Создание окна
WIDTH = 640
HEIGHT = 480
bg_color = 'darkgreen'
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game')
screen = pygame.Surface((WIDTH, HEIGHT))
hero = Player(30, HEIGHT-60)
left = right = up = False
level= [
    '+-------+++-----++++--------++---------++-------+++-----+**+--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------+-',
    '-                                         ***                   +                                                       ******                              -                 +                     -                                                                                    -                               -                                          -                     -*******************************************************   ***-',
    '-   -+-              --+       + + * -  -       -++-            -                                                            *                              +           +---- +                     -                                                                               ------                               -                                          -                     -  ---  -  *    +   -  +                              **     x-',
    '+                                           ++ -        +  +-                                                                *                              +         +     - +                     +     +           *                                                          -**                                                                                -                     -  -    +  - *  -  - + +      -                        *   ----',
    '-       *          ++           *        *-+    *   --+-                      =           =                ==         +   ** *                              -       -       - +                     +       +       +                                                         +**                                        --------                                   -                     -  ++   -  -   *+  --+ +             +         --++-          -',
    '-      +--++               ++        +--                                                            +*                *      *                              +   -++         +*+                     +         -   *                     -*-*-*-*-*-**-*-*-*-*-*-*         --*                                            -                                          -                     -  +    +  +    +  + + +++                  +         -+--    -',
    '*                   --            -+         ---  +     -*--+--+ + - -* --+--**--++++--*--*-++-+*-+++ -++*-+****+-* -**      *                                       +       +                      -          -      -*---*-+-*-+-*-+-                             -*++--*                                ++++++ +----- ----*---                                   -                     -+++--+++-+---+++**-++                          +-+-        ---',
    '--+-    *    +                         *   -    **     +        ****** *    **                                     *         *              -++*-   -+ *    -            -*-*-*+     +*-  -    *   +      -                  -                          -*                                     +*     + +    - -       -                            ---   -                  +-+-                                                                       -',
    '-               +-            -+-*    -++-          +-          +           **                                               *                          *****                --  +          --   +  -      +         -    -----   ++--  *                      --*                                     -*       + +    - -        -                        ---*  -  -   +-            +-  -                            --*++*-+*+-*--  +  -  -+  +*++   -',
    '-   --+-               -                     **--+              +            *                                               *                      -       +          ++++                      +  -        -        --   *   * *       -                  --*                                      -*         + +    - -         --                    --*     -  -*********************-                     -*+-*-*                * *********** -  -',
    '+                           +       --                          +*  -+-           --+-+-**+-**-*-++-* -* -+*+-+-++--++++--++-*                              -  -*+ +-- *                         +  -           -        +     * *        +              --*                                       -*           + +    - -         **--                --*       -  -+++++++++++++++++-----**               --**      *             ----           *   --',
    '-      ---            --+-      --     +--**                    -    +           *                   *  *                                        *   +      +-                                                         -       * *         *          --*                                        +*                                    ---           --*         -                              ---*-*+- *-*          +          *++               * -  -',
    '-+               -+                 *          +--+             -    ++-       ++                                                                 -         -                                                   ---+++         * *           -*+-  --                                          +*                                         --       --*           -                           ---*       *                     *++                  *   --',
    '-        -+-*+                            -++-                  -       +***-+*                     -++                                             +       +                                                                  * *                                                           +*                                               -----*             ----+*--*-*--*--*+-*+--*++--*                             +-*+-+---+--+----++-+-+-* -  -',
    '-                   -*+    --+-    -+     *                     +                              +--*                                               -         --+                     +*-*+--+     +++++---+-**+--                                                                           +*                   -+-                       ---*                                                                        * ++++--++-++--+---+----++-+-*   --',
    '-     -*+                                      -++-             -+++                    *++-                                                               +              - -  +--          *****              ++--**-  -  -  -+++-+  -  - *+ *-*+**--++--  +  +  +  +  +  - - -  -*+-+*+                                             ---+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------++-+++--+--++-----*                            * -  -',
    '-               -++---        ---+     +-        **   -         -                      -                           *+--*+ +--                 *-+-          *--+     +**+                                             ++                                                                   +                                        ---*                                                                                                           *   --',
    '++-                                         *+-         +       +    ++        -++  +-                         -++            +--          -+*         ----      -  -                                                                                                                       *+*++**++**------         -----**------                                                                                                                     -',
    '-        --   **         ++--+            +--   ++--       -    -       ---+       **  *                 -  -                     +--**+--            -     * +- ****   ***   ***    **                         ************************************************************************                     *********              +++**++**++**+++**---*---*---*---*---*---*---*---*---*---*---*---*---*+++*+++*+++*+++*-+-*+--*-+-*-++*-+*-++*--*+-+--',
    '---+--**-----+++-----*+------++---*--++-+-------+++-******************************************************************************+-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------++-------+++-----++++--------++---------+-',]
"""
level= [
    '=-------===-----====--------==---------=',
    '-                                     x-',
    '-   -=-              --=       ==      =',
    '=           --                         -',
    '-                 ==             --    -',
    '-      =--==               ==        =--',
    '-                   --         -       -',
    '--=-         =                         -',
    '-               =-            -=--     -',
    '-   --=-               -               =',
    '=             =             =          -',
    '-*     ---            --=-      --     -',
    '-=               --                    -',
    '-        -=--=                         -',
    '-                   --=    --=-       --',
    '-     --=                              -',
    '-               -=*---        ---=     -',
    '===                                  -=-',
    '-        --              ==--          =',
    '---=------*--===-------------==------==-',]
"""
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
        elif col == '+':
            pl = Platform2(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == '*':
            pl = Trap(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        elif col == 'x':
            pl = Final_block (x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        x += 30
    y += 30
    x = 0

#pl = pygame.Surface((30, 30))
#pl.fill(pygame.Color('black'))

#hero create

class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x +WIDTH/2
    t = -target_rect.y + HEIGHT/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width-WIDTH), l)
    t = max(-(camera.height-HEIGHT), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

total_level_width=len(level[0])*30
total_level_height=len(level)*30

camera = Camera(camera_func, total_level_width, total_level_height)
#end_game = False
timer = pygame.time.Clock()
sound.play()
while not hero.end_game:
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

            
    #print(num)
    screen.fill(pygame.Color(bg_color))
    #create_lvl(level1, pl)
    #sprite_group.draw(screen)
    coin_group.draw(screen)
    hero.update(left, right, up, platforms)
    camera.update(hero)
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))
    #sprite_group.draw(screen)
    #coin_group.draw(screen)

    window.blit(screen, (0, 0))

    pygame.display.flip()
    timer.tick(70)
    
