import pygame
#from button import Button

#initialize python
pygame.init()

clock = pygame.time.Clock()
FPS = 60

#window dimensions
screen_w = 500
screen_h = 720

#create window
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Dumpster Dash')

#button initialize
menu_logo_img = pygame.image.load('assets/logos_and_icons/menu_logo.png').convert_alpha()
play_button_img = pygame.image.load('assets/logos_and_icons/play.png').convert_alpha()
quit_button_img = pygame.image.load('assets/logos_and_icons/quit.png').convert_alpha()
restart_button_img = pygame.image.load('assets/logos_and_icons/restart.png').convert_alpha()
game_over_img = pygame.image.load('assets/logos_and_icons/game_over.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw (self):
        
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Logo():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw (self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


#draw logo
menu_logo = Logo(250, 200, menu_logo_img)

#gameloop
play_button = Button(250, 500, play_button_img)
quit_button = Button(250, 600, quit_button_img)

#scrolling background
bg_image = pygame.image.load('assets/bg.png').convert()
overlap_bg_image = pygame.image.load('assets/bg.png').convert()
b_pos = 0
o_pos = 720
speed = 7

#loop to retain screen
gamerun = True
while gamerun:
    clock.tick(FPS)  # FPS of game

    #Draw scrolling background
    if b_pos >= screen_h:
        b_pos = -screen_h
    if o_pos >= screen_h:
        o_pos = -screen_h
        
    b_pos += speed
    o_pos += speed
    screen.blit(bg_image, (0, b_pos))
    screen.blit(overlap_bg_image, (0, o_pos))

    menu_logo.draw()
    if play_button.draw():
        print ('this is the game')#game here
    if quit_button.draw():
        gamerun = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False

    # Update display window
    pygame.display.update()