from pygame.sprite import Sprite, collide_rect
from pygame import Surface, mixer 
import pyganim
from pygame import Color
from platforms import *
from time import sleep

mixer.pre_init(44100, -16, 1, 512)
mixer.init()

move_speed = 5
gravity = 0.6
jump = 9.9
c = 'darkgreen'

anim_delay = 0.08
anim_stay = [('images/Hero/11.png', anim_delay)]

anim_right = ['images/Hero/r2.png',
              'images/Hero/r3.png',
              'images/Hero/r4.png',
              'images/Hero/r5.png',
              'images/Hero/r6.png',
              'images/Hero/r7.png',
              'images/Hero/r8.png']

anim_left = ['images/Hero/l2.png',
              'images/Hero/l3.png',
              'images/Hero/l4.png',
              'images/Hero/l5.png',
              'images/Hero/l6.png',
              'images/Hero/l7.png',
              'images/Hero/l8.png',]

anim_jump = [('images/Hero/jump.png', anim_delay)]
anim_jump_r = [('images/Hero/rjump.png', anim_delay)]
anim_jump_l = [('images/Hero/ljump.png', anim_delay)]

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((17, 28))
        # self.image.fill((0, 130, 130))
        self.a = 0 
        self.g = 0
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

        self.onPlatform = False

        def make_Anim(anim_list, delay):
            anim_final = []
            for anim in anim_list:
                anim_final.append((anim, delay))
            anim_result = pyganim.PygAnimation(anim_final)
            return anim_result

        self.Anim_Stay = pyganim.PygAnimation(anim_stay)
        self.Anim_Stay.play()
        
        self.Anim_Right = make_Anim(anim_right, anim_delay)
        self.Anim_Right.play()

        self.Anim_Left = make_Anim(anim_left, anim_delay)
        self.Anim_Left.play()

        self.Anim_jump = pyganim.PygAnimation(anim_jump)
        self.Anim_jump.play()
        self.jump_sound = mixer.Sound('sounds/jump.ogg')

        self.Anim_jump_r = pyganim.PygAnimation(anim_jump_r)
        self.Anim_jump_r.play()

        self.Anim_jump_l = pyganim.PygAnimation(anim_jump_l)
        self.Anim_jump_l.play()

        self.death_sound = mixer.Sound('sounds/IOUS.ogg')
        self.final_sound = mixer.Sound('sounds/welldone.ogg')

        self.end_game = False

        

    def update(self, left, right, up, platforms):

        if up:
            if self.onPlatform:
                self.g = -jump
                self.jump_sound.play()
            self.image.fill(Color(c))
            self.Anim_jump.blit(self.image, (0, 0))
            
        if left:
            self.a = -move_speed
            self.image.fill(Color(c))
            if up:
                self.Anim_jump_l.blit(self.image, (0, 0))
                #self.jump_sound.play()
            else:
                self.Anim_Left.blit(self.image, (0, 0))
        if right:
            self.a = move_speed
            self.image.fill(Color(c))
            if up:
                self.Anim_jump_r.blit(self.image, (0, 0))
                #self.jump_sound.play()
            else:
                self.Anim_Right.blit(self.image, (0, 0))
        if not(left or right):
            self.a = 0
            if not up:
                self.image.fill(Color(c))
                self.Anim_Stay.blit(self.image, (0, 0))



        if not self.onPlatform:
            self.g += gravity  # ускорение свободного падения

        self.onPlatform = False
        self.rect.x += self.a
        self.collide(self.a, 0, platforms)
        self.rect.y += self.g
        self.collide(0, self.g, platforms)
            
    def collide(self, a, g, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if isinstance(pl, Trap): 
                    self.die()
                elif isinstance(pl, Final_block):
                    self.win()
                else:
                    if a > 0:
                        self.rect.right = pl.rect.left
                    if a < 0:
                        self.rect.left = pl.rect.right
                    if g > 0:
                        self.rect.bottom = pl.rect.top
                        self.onPlatform = True
                        self.g = 0
                    if g < 0:
                        self.rect.top = pl.rect.bottom
                        self.g = 0

    def gotostart(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
        
    def die(self):
        self.death_sound.play()
        sleep(3)
        self.gotostart(self.x, self.y)

    def win(self):
        #self.final_sound.play()
        sleep(3)
        self.end_game = True
        
