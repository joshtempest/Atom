import pygame
import keyboard

running = True

pygame.init()
screen = pygame.display.set_mode((1000,1000))
textfont = pygame.font.SysFont(None, 32)
img = textfont.render('hello', True, pygame.Color('blue'))
while running == True:
    screen.blit(img, (200, 200))
    pygame.display.flip()
    if keyboard.is_pressed('esc'):
        running = False
