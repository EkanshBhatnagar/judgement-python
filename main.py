from classes import *
import pygame
from tkinter import *
import sys


def Game(no_of_players,max_cards):
    pygame.init()
    sc_width, sc_height = 1280, 720
    base_font = pygame.font.Font('arial.ttf',32)
    user_text = ''
    input_rect = pygame.Rect(640,360,140,32)
    main_deck = CardStack()
    main_deck.make_full_deck()
    main_deck.deck_shuffle()

    clock = pygame.time.Clock()

    game_display = pygame.display.set_mode((sc_width,sc_height))
    pygame.display.set_caption('Judgement')
    deck_img = pygame.image.load("JPEG/Red_back.jpg").convert_alpha()
    deck_img = pygame.transform.scale(deck_img, (100,150))
    game_display.fill((3,103,0))
    players = []
    for i in range(no_of_players):
        players.append(CardStack())
    
    main_deck.deal(players[0],2)
    for card in players[0].cards:
        print(card.__str__().__str__())
    active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        game_display.blit(deck_img,(200,200))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()