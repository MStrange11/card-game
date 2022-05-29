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
card_back_img = pygame.image.load('card_back.png').convert_alpha()
mode01_img = pygame.image.load('mode01.jpg').convert_alpha()
mode02_img = pygame.image.load('mode02.jpg').convert_alpha()
mode03_img = pygame.image.load('mode03.jpg').convert_alpha()
mode04_img = pygame.image.load('mode04.png').convert_alpha()









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
    def __init__(self):
        self.deck = []
        

    def rand(self, runn):
        self.decklen = len(self.deck)
        print(self.decklen) 
        if self.decklen < 53:
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
                card_text = print(f"the card is {color} {symbol} {number}") 
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
        else :
            print("No more card left in the deck")
        scale_width = 180 
        scale_height = scale_width * 3 / 2          
        card1 = pygame.transform.scale(card0, (scale_width, scale_height))
        self.deck.append(card0)

        #text loading
        # font =  pygame.font.Font('freesansbold.ttf', 32)
        # text = font.render(card_text, True, (0, 255, 0), (0, 0, 255))
        # textRect = text.get_rect()

        return card1
         
class player():
    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []

    def RUN(self, card_pic, text):
        # self.image2 = card_pic
        screen.blit(card_pic, (45, 45))
        self.player1.append(card_pic)
        print(len(self.player1) - 1)
        screen.blit(text, (1160, 400))

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

# font =  pygame.font.Font('freesansbold.ttf', 32)
# text = font.render( True, (0, 255, 0), (0, 0, 255))

#Labling
start_button = Buttom(500, 250, start_img, 1)
exit_button = Buttom(1180, 595, exit_img, 0.4)
turn_button = Buttom(1130, 90, turn_img, 0.7)
mode01_button = Buttom(500, 100, mode01_img, 0.5)
mode02_button = Buttom(700, 100, mode02_img, 0.5)
mode03_button = Buttom(500, 300, mode03_img, 0.7)
mode04_button = Buttom(700, 300, mode04_img, 0.1)
turn_butt = comp()
card_picture = player()
player1 = player()
player2 = player()
player3 = player()
player4 = player()



#setting up condition
start = False
mainu = True
runn = False
modes = False
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
            modes = True



    # if mainu == False:
    #     mode01_button.draw(screen)
    #     mode02_button.draw(screen)
    #     mode03_button.draw(screen)
    #     mode04_button.draw(screen)
    #     if mode01_button.draw(screen):
    #         print("mode01 activated")
    #     elif mode02_button.draw(screen):
    #         print("mode02 activated")
    #     elif mode03_button.draw(screen):
    #         print("mode03 activated")
    #     elif mode04_button.draw(screen):
    #         print("mode04 activated")    
        
    
    if modes == True:    
        bg_image2 = pygame.transform.scale(bg_image0, (1130, 650))
        screen.blit(bg_image2, (0, 0))
        scale_width = 180 
        scale_height = scale_width * 3 / 2          
        card_back_img = pygame.transform.scale(card_back_img, (scale_width, scale_height))
        screen.blit(card_back_img, (45, 45))
        # text = pygame.transform.scale(text , (100, 30) )
        

        if turn_button.draw(screen):
            print("turn changed")
            runn = True
            if runn == True:
                card_pic = turn_butt.rand(runn)
                runn = False
            card_picture.RUN(card_pic,)
            
            
            

        if exit_button.draw(screen):
            break


    event = pygame.event.wait()
    if event.type == pygame.QUIT:    
        break
    pygame.display.update()

pygame.quit()       