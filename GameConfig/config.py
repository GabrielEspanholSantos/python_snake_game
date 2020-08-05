UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

import pygame
import os
from GameConfig.Fonts import Fonts

screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def print_snake(screen, font_color, snake_font, i):
    snake_font_screen = snake_font.render('Snake Game', True, font_color)
    snake_font_area = snake_font_screen.get_rect()
    snake_font_area.midtop = ((600 // 2)- 5 + (i*10), 60 - (i*10))
    screen.blit(snake_font_screen, snake_font_area)


def create_font(text, style, size, pos):
    font = Fonts(text, style, size)
    font.set_type()
    font.set_render()
    font.set_area()
    font.set_location(mid=pos[0], top=pos[1])
    return font


def alter_font_color(font, color):
    font.set_color(color)
    font.set_render()
    return font


def switch_title(font, color, pos=None):
    font.set_color(color)
    font.set_render()
    
    if pos:
        font.set_location(mid=pos[0], top=pos[1])

    return font