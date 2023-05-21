#import library
import pygame
from pygame.locals import *
import sys

#initialize pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

#window dimensions
screen_w = 500
screen_h = 720

#create window
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Dumpster Dash')

#scrolling background
bg_image = pygame.image.load('assets/bg.png').convert()
overlap_bg_image = pygame.image.load('assets/bg.png').convert()
b_pos = 0
o_pos = 720
speed = 7

#lane coordinates
left_lane = 150
center_lane = 166
right_lane = 275
lanes = [left_lane, center_lane, right_lane]

#wally
class Runner():
    def __init__(self, x, y):
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(16):
            img = pygame.image.load(f'assets/wallyrun/{i}.png')
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def update(self):
        animation_cooldown = 20
        #handle animation
        #update image
        self.image = self.animation_list[self.frame_index]
        #check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            
        #if the animation surpasses last frame, reset
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
    
    def move(self):
        
        for event in pygame.event.get():
      
        # move the player's car using the left/right arrow keys
            if event.type == KEYDOWN:
                if event.key == K_LEFT and wally.rect.center[0] > left_lane:
                    wally.rect.left -= 100
                elif event.key == K_RIGHT and  wally.rect.center[0] < right_lane:
                    wally.rect.right += 100
        
            
            
            
    
    def draw(self):
        screen.blit(self.image, self.rect)
        
wally = Runner(250, 575)
        
#loop to retain screen

gamerun = True
while gamerun:
    
    #pygame.time.delay(60) #pause the program for an amount of time, which uses lots of CPU in a busy loop to make sure that timing is more accurate. 
    
    clock.tick(FPS) #fps of game
    
    wally.move()
    
    #draw scrollbackground
    if b_pos >= screen_h:
        b_pos = -screen_h
    if o_pos >= screen_h:
        o_pos = -screen_h
        
    b_pos += speed
    o_pos += speed
    screen.blit(bg_image, (0, b_pos))
    screen.blit(overlap_bg_image, (0, o_pos))
    
    #wally running
    wally.update()
    wally.draw()
    
    #event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
            sys.exit ()
           
    #update display window
    pygame.display.update()

pygame.QUIT()