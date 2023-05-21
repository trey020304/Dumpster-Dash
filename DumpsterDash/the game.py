#import library
import pygame

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

#wally running
class Player(pygame.sprite.Sprite,):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/frame0000.png'))
        self.sprites.append(pygame.image.load('assets/frame0001.png'))
        self.sprites.append(pygame.image.load('assets/frame0002.png'))
        self.sprites.append(pygame.image.load('assets/frame0003.png'))
        self.sprites.append(pygame.image.load('assets/frame0004.png'))
        self.sprites.append(pygame.image.load('assets/frame0005.png'))
        self.sprites.append(pygame.image.load('assets/frame0006.png'))
        self.sprites.append(pygame.image.load('assets/frame0007.png'))
        self.sprites.append(pygame.image.load('assets/frame0008.png'))
        self.sprites.append(pygame.image.load('assets/frame0009.png'))
        self.sprites.append(pygame.image.load('assets/frame0010.png'))
        self.sprites.append(pygame.image.load('assets/frame0011.png'))
        self.sprites.append(pygame.image.load('assets/frame0012.png'))
        self.sprites.append(pygame.image.load('assets/frame0013.png'))
        self.sprites.append(pygame.image.load('assets/frame0014.png'))
        self.sprites.append(pygame.image.load('assets/frame0015.png'))
        self.sprites.append(pygame.image.load('assets/frame0016.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    
    def update(self):
        self.current_sprite += .6
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        self.image = self.sprites[int(self.current_sprite)]
        
#wally running - sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(250,575)
moving_sprites.add(player)

#igagalaw si wally
#def move(self):
    
#scrolling background
bg_image = pygame.image.load('assets/bg.png').convert()
overlap_bg_image = pygame.image.load('assets/bg.png').convert()
b_pos = 0
o_pos = 720
speed = 7

#loop to retain screen

#wally = Player(player)

gamerun = True
while gamerun:
    
    #pygame.time.delay(60) #pause the program for an amount of time, which uses lots of CPU in a busy loop to make sure that timing is more accurate. 
    
    clock.tick(FPS) #fps of game
    
    #draw scrollbackground
    if b_pos >= screen_h:
        b_pos = -screen_h
    if o_pos >= screen_h:
        o_pos = -screen_h
        
    b_pos += speed
    o_pos += speed
    screen.blit(bg_image, (0, b_pos))
    screen.blit(overlap_bg_image, (0, o_pos))
    
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    
    #event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
           
    #update display window
    pygame.display.update()

pygame.QUIT()