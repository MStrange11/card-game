import pygame
import random
import os
import back_end

game_pack = []
dealt_cards = []
card_dir = " "
game_start = False
card_position = ""
counter = 0
automatic_deal_time = 0
automatic_dealer_dealing = False
row_A, row_B, row_C = None, None, None
FPS = 0

MAIN_FILE_PATH = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(MAIN_FILE_PATH, "images")
ICON_FOLDER = os.path.join(MAIN_FILE_PATH, "icon")
CARDS_FOLDER = os.path.join(IMAGES_FOLDER, "cards")
print(ICON_FOLDER)

# Title and icon
pygame.display.set_caption("Card Trick")
icon = pygame.image.load(os.path.join(
    ICON_FOLDER, "steve.jpg"))
pygame.display.set_icon(icon)

# Cards dictionary import
CARDS = back_end.cards()

# Color import
COLORS = back_end.colors()

pygame.font.init()
WIDTH, HEIGHT = 1200, 850
CARD_W, CARD_H = 100, 133
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGES_FOLDER, "table_top.png")), (WIDTH, HEIGHT))

# Font definition
smallText = pygame.font.Font('freesansbold.ttf', 25)

# Cursor
pygame.mouse.set_cursor(*pygame.cursors.tri_left)


def gamePack():
    global game_pack, dealt_cards
    game_pack = []
    dealt_cards = []

    while len(game_pack) < 21:
        new_card = random.choice([x for x in CARDS.keys()])
        if new_card not in game_pack and new_card != "purple_back":
            game_pack.append(new_card)

    for i in game_pack:
        i = CARD(i)
        dealt_cards.append(i)


def text_objects(text, font):
    text_surface = (font.render(text, True, COLORS["white"]))
    return text_surface, text_surface.get_rect()


class CARD:
    def __init__(self, card_name, new_x=50, new_y=50, x=50, y=50):
        self.card_name = card_name
        self.x = x
        self.y = y
        self.new_x = new_x
        self.new_y = new_y
        self.img = pygame.transform.scale(pygame.image.load(
            os.path.join(CARDS_FOLDER, CARDS[self.card_name])), (CARD_W, CARD_H))

    def draw_card(self, window):
        window.blit(self.img, (self.x, self.y))

    def cards_move(self, vel, card_dir):
        if card_dir == "out":
            if self.new_x > self.x and self.new_y > self.y:
                self.x += vel
                self.y += vel
            elif self.new_x != self.x:
                self.x += vel
            elif self.new_y != self.y:
                self.y += vel

        if card_dir == "in":
            if self.new_x != self.x and self.new_y != self.y:
                self.x -= vel
                self.y -= vel
            elif self.new_y != self.y:
                self.y -= vel
            elif self.new_x != self.x:
                self.x -= vel


class Buttons:
    def __init__(self, name, btnLbl, button_x, button_y, button_length, button_width, inactive, active):
        self.name = name
        self.btnLbl = btnLbl
        self.button_x = button_x
        self.button_y = button_y
        self.button_length = button_length
        self.button_width = button_width
        self.inactive = inactive
        self.active = active

    def button_animation(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_x + self.button_length > mouse_pos[0] > self.button_x and self.button_y + self.button_width > \
                mouse_pos[1] > self.button_y:
            pygame.draw.rect(WIN, self.active, (self.button_x, self.button_y, self.button_length, self.button_width))
        else:
            pygame.draw.rect(WIN, self.inactive, (self.button_x, self.button_y, self.button_length, self.button_width))

        textSurf, textRect = text_objects(self.btnLbl, smallText)
        textRect.center = ((self.button_x + self.button_length // 2), (self.button_y + self.button_width // 2))
        WIN.blit(textSurf, textRect)

    def button_click(self):
        global card_position, automatic_dealer_dealing
        global row_A, row_B, row_C, dealt_cards, counter, automatic_deal_time, game_start
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.button_x + self.button_length > mouse_pos[0] > self.button_x and self.button_y + self.button_width > \
                mouse_pos[1] > self.button_y:
            if mouse_click[0] == 1 and self.name == "game_start" and counter < 3:
                cards_display()
            if mouse_click[0] == 1 and self.name == "choice" and dealt_cards[0].x == 110:
                row_A, row_B, row_C = back_end.lists_formation(dealt_cards)
                reform_pack()
                cards_display_pack()
                automatic_deal_time = 0
                automatic_dealer_dealing = True
                game_start = True

            if mouse_click[0] == 1 and self.name == "game_restart":
                gamePack()
                game_start = False
                counter = 0

            if mouse_click[0] == 1 and self.name in ["a", "b", "c"] and dealt_cards[0].x == 280:
                dealt_cards = []
                dealt_cards = back_end.positioning(row_A, row_B, row_C, self.name.upper())
                counter += 1
                if counter < 3:
                    row_A, row_B, row_C = back_end.lists_formation(dealt_cards)
                    reform_pack()
                    cards_display_pack()
                    automatic_deal_time = 0
                    automatic_dealer_dealing = True
                else:
                    cards_display_pack()
                    automatic_deal_time = 0
                    automatic_dealer_dealing = True


def reform_pack():
    global dealt_cards
    dealt_cards = []
    for i in row_A:
        dealt_cards.append(i)
    for j in row_B:
        dealt_cards.append(j)
    for k in row_C:
        dealt_cards.append(k)


def automaticDealer():
    global automatic_dealer_dealing, FPS
    if automatic_dealer_dealing:
        if counter < 3:
            if automatic_deal_time == FPS * 4:
                cards_display_by_rows()
            if automatic_deal_time == FPS * 8:
                automatic_dealer_dealing = False

        elif counter == 3:
            if automatic_deal_time == FPS * 4:
                result_display()
            if automatic_deal_time == FPS * 8:
                dealt_cards[10].img = pygame.transform.scale(pygame.image.load
                                                             (os.path.join(CARDS_FOLDER,
                                                                           CARDS[dealt_cards[10].card_name])),
                                                             (CARD_W, CARD_H))


def create_buttons():
    button_dictionary = {
        "game_start": Buttons("game_start", "Start", 940, 80, 110, 50, COLORS["dark_orange"], COLORS["light_orange"]),
        "game_restart": Buttons("game_restart", "Restart", 1060, 80, 110, 50, COLORS["dark_orange"],
                                COLORS["light_orange"]),
        "choice": Buttons("choice", "I made my choice", 940, 160, 230, 50, COLORS["dark_orange"],
                          COLORS["light_orange"]),
        "a": Buttons("a", "A", 1030, 275, 100, 50, COLORS["dark_purple"], COLORS["light_purple"]),
        "b": Buttons("b", "B", 1030, 425, 100, 50, COLORS["dark_purple"], COLORS["light_purple"]),
        "c": Buttons("c", "C", 1030, 575, 100, 50, COLORS["dark_purple"], COLORS["light_purple"]),
    }

    for button in button_dictionary:
        if not game_start:
            button_dictionary[button].button_animation()
            button_dictionary[button].button_click()
        elif game_start and button_dictionary[button].name not in ["choice", "game_start"]:
            button_dictionary[button].button_animation()
            button_dictionary[button].button_click()


def cards_display_pack():
    global dealt_cards, card_dir
    card_dir = "in"
    for i in dealt_cards:
        i.new_x = 50
        i.new_y = 50


def cards_display():
    global dealt_cards, card_dir
    card_dir = "out"
    x_cards = 110
    for i in dealt_cards:
        if i.x == 50 and i.y == 50:
            i.new_x = x_cards
            i.new_y = 390
        x_cards += 40


def cards_display_by_rows():
    global dealt_cards, card_dir
    card_dir = "out"
    counter = 0
    start_x = 280
    start_y = 240

    for i in range(3):
        for j in range(7):
            if dealt_cards[counter].x == 50 and dealt_cards[counter].y == 50:
                dealt_cards[counter].new_x = start_x
                dealt_cards[counter].new_y = start_y
            counter += 1
            start_x += 100
        start_x = 280
        start_y += 150


def result_display():
    global dealt_cards, card_dir
    card_dir = "out"
    dealt_cards[10].img = pygame.transform.scale(pygame.image.load(
        os.path.join(CARDS_FOLDER, "purple_back.png")), (CARD_W, CARD_H))
    dealt_cards[10].new_x = 580
    dealt_cards[10].new_y = 390


def main():
    global automatic_deal_time, card_dir, FPS
    run = True
    FPS = 60
    cards_speed = 5
    clock = pygame.time.Clock()
    gamePack()

    def redraw():
        WIN.blit(BG, (0, 0))
        for i in dealt_cards:
            i.draw_card(WIN)
            i.cards_move(cards_speed, card_dir)

        create_buttons()
        automaticDealer()
        pygame.display.update()

    while run:
        clock.tick(FPS)
        automatic_deal_time += 1
        redraw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            cards_display()
        if key[pygame.K_a]:
            cards_display_pack()
        if key[pygame.K_b]:
            cards_display_by_rows()
