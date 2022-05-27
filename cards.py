import pygame
import random

class RAND():
    def rand(self):
        sym = [3, 4, 5, 6] #[club, spade, diamond, heart] 
        colr = ["red", "black"]   
        card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        symbol = (random.choice(sym)) 
        color = (random.choice(colr))
        number = (random.choice(card))
        # print(f"the card is {color} {symbol} {number}")

        if color == "black":
            if symbol == 3:
                for i in range(1, 14):
                    card = pygame.image.load(f"blackclub{i}.png")
            elif symbol == 4:
                for i in range(1, 14):
                    card = pygame.image.load(f"blackspade{i}.png")
        elif color == "red":
            if symbol == 5:    
                for i in range(1, 14):
                    card = pygame.image.load(f"reddiamond{i}.png")
            elif symbol == 6:    
                for i in range(1, 14):
                    card = pygame.image.load(f"redheart{i}.png")   

        return card    