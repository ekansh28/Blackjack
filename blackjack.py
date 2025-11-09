import copy
import pygame
import random

#Variables
cards = ['2','3','4','5','6','7','8','9','10','J','K','Q','A']
one_deck = 4 * cards
game_deck = 4

# Overall Game Record (Win, Loss, Tie)
records = [0,0,0]
player_score = 0
dealer_score = 0
#GUI initialization
pygame.init()
WIDTH = 600
HEIGHT = 900

FPS = 60
timer = pygame.time.Clock()



active = False
initial_deal = False
game_decks = game_deck * one_deck
my_hand = []
dealer_hand = []

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('BlackJack')
font = pygame.font.Font('freesansbold.ttf',44)



def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    return current_hand, current_deck

def draw_button(color, border_color, rect, text, text_color='black', border_width=3, corner_radius=5):
    """
    Draws a button with text on the screen.
    Returns the button rect (so you can detect clicks later).
    """

    # Draw filled rectangle (button background)
    button = pygame.draw.rect(screen, color, rect, 0, corner_radius)

    # Draw border (optional)
    pygame.draw.rect(screen, border_color, rect, border_width, corner_radius)

    # Render and center text
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(rect[0] + rect[2]//2, rect[1] + rect[3]//2))
    screen.blit(text_surf, text_rect)

    return button

# Drawing Game Conditions and Buttons
def draw_game(act):
    button_list = []
    # if hands empty
    if not act:
        deal = draw_button(
            color='white',
            border_color='green',
            rect=[150, 20, 300, 100],
            text='Deal Hand'
        )
        button_list.append(deal)
    else:
        hit = draw_button(
            color = 'white',
            border_color='green',
            rect=[20,700,250,90],
            text='HIT'
        )
        button_list.append(hit)
        stand = draw_button(
            color = 'white',
            border_color='red',
            rect = [ 330, 700 , 250 , 90],
            text='STAND'
        )
        button_list.append(stand)
    return button_list


#Game Initialization
run = True
while run:
    timer.tick(FPS)
    screen.fill('black')


    if initial_deal:
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        initial_deal = False
    buttons = draw_game(active)

    text_surf = font.render(f"Win : {records[0]} Loss : {records[1]} Tie : {records[2]}", True, "white")
        
    # Get the rectangle of the text (for positioning)
    text_rect = text_surf.get_rect(center=(WIDTH // 2, HEIGHT - 30))

    # Draw (blit) it on screen
    screen.blit(text_surf, text_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_decks = game_deck * one_deck
                    my_hand = []
                    dealer_hand = []
                    
    
    pygame.display.flip()
pygame.quit()
