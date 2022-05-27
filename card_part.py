import pygame
import random
import time

pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(u'Testing deck of cards')

my_card = None


#load all images {#black [club, spade,] and red [diamond, heart]}
class load_cards():
    def deck_of_cards(self, runn):
        #load all black club
        BC1 = pygame.image.load('blackclub1.png')
        BC2 = pygame.image.load('blackclub2.png')
        BC3 = pygame.image.load('blackclub3.png')
        BC4 = pygame.image.load('blackclub4.png')
        BC5 = pygame.image.load('blackclub5.png')
        BC6 = pygame.image.load('blackclub6.png')
        BC7 = pygame.image.load('blackclub7.png')
        BC8 = pygame.image.load('blackclub8.png')
        BC9 = pygame.image.load('blackclub9.png')
        BC10 = pygame.image.load('blackclub10.png')
        BC11 = pygame.image.load('blackclub11.png')
        BC12 = pygame.image.load('blackclub12.png')
        BC13 = pygame.image.load('blackclub13.png')

        #load all black spade
        BS1 = pygame.image.load('blackspade1.png')
        BS2 = pygame.image.load('blackspade2.png')
        BS3 = pygame.image.load('blackspade3.png')
        BS4 = pygame.image.load('blackspade4.png')
        BS5 = pygame.image.load('blackspade5.png')
        BS6 = pygame.image.load('blackspade6.png')
        BS7 = pygame.image.load('blackspade7.png')
        BS8 = pygame.image.load('blackspade8.png')
        BS9 = pygame.image.load('blackspade9.png')
        BS10 = pygame.image.load('blackspade10.png')
        BS11 = pygame.image.load('blackspade11.png')
        BS12 = pygame.image.load('blackspade12.png')
        BS13 = pygame.image.load('blackspade13.png')

        #load all Red heart
        RH1 = pygame.image.load('redheart1.png')
        RH2 = pygame.image.load('redheart2.png')
        RH3 = pygame.image.load('redheart3.png')
        RH4 = pygame.image.load('redheart4.png')
        RH5 = pygame.image.load('redheart5.png')
        RH6 = pygame.image.load('redheart6.png')
        RH7 = pygame.image.load('redheart7.png')
        RH8 = pygame.image.load('redheart8.png')
        RH9 = pygame.image.load('redheart9.png')
        RH10 = pygame.image.load('redheart10.png')
        RH11 = pygame.image.load('redheart11.png')
        RH12 = pygame.image.load('redheart12.png')
        RH13 = pygame.image.load('redheart13.png')

        #load all Red diamond
        RD1 = pygame.image.load('reddiamond1.png')
        RD2 = pygame.image.load('reddiamond2.png')
        RD3 = pygame.image.load('reddiamond3.png')
        RD4 = pygame.image.load('reddiamond4.png')
        RD5 = pygame.image.load('reddiamond5.png')
        RD6 = pygame.image.load('reddiamond6.png')
        RD7 = pygame.image.load('reddiamond7.png')
        RD8 = pygame.image.load('reddiamond8.png')
        RD9 = pygame.image.load('reddiamond9.png')
        RD10 = pygame.image.load('reddiamond10.png')
        RD11 = pygame.image.load('reddiamond11.png')
        RD12 = pygame.image.load('reddiamond12.png')
        RD13 = pygame.image.load('reddiamond13.png')

        deck = {BC1, BC2, BC3, BC4, BC5, BC6, BC7, BC8, BC9, BC10, BC11, BC12, BC13,
                BS1, BS2, BS3, BS4, BS5, BS6, BS7, BS8, BS9, BS10, BS11, BS12, BS13, 
                RD1, RD2, RD3, RD4, RD5, RD6, RD7, RD8, RD9, RD10, RD11, RD12, RD13, 
                RH1, RH2, RH3, RH4, RH5, RH6, RH7, RH8, RH9, RH10, RH11, RH12, RH13 }
        if runn == True:
            my_card = (random.choice(deck))
        return my_card

cardd = load_cards()

runn = True
#main code
while True:
    screen.fill((225, 225, 235))
    card = cardd.deck_of_cards(runn)
    runn = False
    print(f"Your card is {card}")



    event = pygame.event.wait()
    if event.type == pygame.QUIT:    
        break
    pygame.display.update()

pygame.quit() 