import random
import pygame
from pygame.locals import *
from pygame import mixer
from os import path

pygame.init()
mixer.init()
clock = pygame.time.Clock()
fps = 60


SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
pygame.display.set_caption(u'lets play cards') 

#load control buttons image
bg_image0 = pygame.image.load('grassmat.jpg')
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
turn_img = pygame.image.load('your-turn.jpg').convert_alpha()

class Buttom():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True    
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False  

        surface.blit(self.image, self.rect)
        return action
        
class comp():
    def rand(self, runn):
        if runn == True:
            sym = ["club", "spade", "diamond", "heart"] 
            # colr = ["red", "black"]   
            card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
            # color = (random.choice(colr))
            number = (random.choice(card_num))
            symbol = (random.choice(sym))
            if symbol == "club" or symbol == "spade":
                color = "black"
            elif symbol == "diamond" or symbol == "heart":
                color = "red"    
            print(f"the card is {color} {symbol} {number}")  
            runn = False
        

        
        if symbol == "club":
            if number > 0 and number < 14:
                card0 = pygame.image.load(f"blackclub{number}.png")
        elif symbol == "spade":
            if number > 0 and number < 14:
                card0 = pygame.image.load(f"blackspade{number}.png")
        
        if symbol == "diamond":    
            if number > 0 and number < 14:
                card0 = pygame.image.load(f"reddiamond{number}.png")
        elif symbol == "heart":    
            if number > 0 and number < 14:
                card0 = pygame.image.load(f"redheart{number}.png")

        scale_width = 180 
        scale_height = scale_width * 3 / 2          
        card1 = pygame.transform.scale(card0, (scale_width, scale_height))          
        return card1
         
class player():
    def RUN(self, card_pic ):
        # self.image2 = card_pic
        screen.blit(card_pic, (45, 45))

# def fade(width, height): 
#     fade = pygame.Surface((width, height))
#     fade.fill((0,0,0))
#     for alpha in range(0, 300):
#         fade.set_alpha(alpha)
#         redrawWindow()
#         screen.blit(fade, (0,0))
#         pygame.display.update()
#         pygame.time.delay(5)

# def redrawWindow():
#     screen.fill((255, 255, 255))

#Labling
start_button = Buttom(500, 250, start_img, 1)
exit_button = Buttom(1180, 595, exit_img, 0.4)
turn_button = Buttom(1130, 90, turn_img, 0.7)
turn_butt = comp()
card_picture = player()

#setting up condition
start = False
mainu = True
runn = False
options = False
card_pic = None
game_mode1 = False
game_mode2 = False
game_mode3 = False
game_mode4 = False

#main code
while True:
    # redrawWindow()
    clock.tick(fps)
    screen.fill((179, 220, 109))
    if mainu == True:
        if start_button.draw(screen):
            start = True
            # fade(1280, 650)
            print("Starting the game")
            mainu = False

    if mainu == False:
        
        bg_image2 = pygame.transform.scale(bg_image0, (1130, 650))
        screen.blit(bg_image2, (0, 0))

        if turn_button.draw(screen):
            print("turn changed")
            runn = True
            if runn == True:
                card_pic = turn_butt.rand(runn)
                runn = False
            card_picture.RUN(card_pic)
            

        if exit_button.draw(screen):
            break


    event = pygame.event.wait()
    if event.type == pygame.QUIT:    
        break
    pygame.display.update()

pygame.quit()       