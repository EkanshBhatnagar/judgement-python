from classes import *
import pygame
import sys
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
active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
           if input_rect.collidepoint(event.pos):
                active = True
           else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode



    game_display.fill((3,103,0))
    pygame.draw.rect(game_display,(255,255,255), input_rect)
    text_surface = base_font.render(user_text,True, (0,0,0))
    game_display.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)

    #game_display.blit(deck_img,(200,200))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()