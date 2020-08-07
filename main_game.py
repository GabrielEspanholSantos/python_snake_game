import os
dir_name = os.path.join(os.path.dirname(__file__))

import pygame
from pygame.locals import *

from Snake import Snake
from Apple import Apple
from GameConfig.config import *

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2)
pygame.mixer.init()
pygame.display.set_caption('Snake')


def play_game(best_score):
    pygame.time.wait(200)
    pygame.mixer.music.load('GameSounds/happy-cave.ogg')
    pygame.mixer.music.play(-1)

    snake = Snake(head=(200, 200), mid=(210, 200), tail=(220,200), head_color=(255, 102, 0), body_color=(255, 153, 3))

    apple = Apple()

    my_direction = LEFT
    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0
    dead_line = False

    while True:
        clock.tick(snake.get_speed())
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_KP8) and my_direction != DOWN:
                    my_direction = UP
                    break
                elif (event.key == K_DOWN or event.key == K_KP2) and my_direction != UP:
                    my_direction = DOWN
                    break
                elif (event.key == K_LEFT or event.key == K_KP4) and my_direction != RIGHT:
                    my_direction = LEFT
                    break
                elif (event.key == K_RIGHT or event.key == K_KP6) and my_direction != LEFT:
                    my_direction = RIGHT
                    break

        if collision(snake.get_snake()[0], apple.get_apple_pos()):
            pygame.mixer.Sound.play(pygame.mixer.Sound("GameSounds/carrot.ogg"))
            apple.create()
            snake.increase_size()
            score += 1

        snake.update_location(my_direction)

        snake_head = snake.get_snake()[0]
        if list(filter(lambda part: collision(snake_head, part), snake.get_snake()[1:])):
            dead_line = True
        
        if ((snake_head[0] == 600 or snake_head[1] == 600) or (snake_head[0] == 0 or snake_head[1] == 0)):
            dead_line = True

        screen.fill((51, 204, 51))
        screen.blit(apple.get_apple(), apple.get_apple_pos())
        # pygame.draw.circle(screen, apple.get_color(), apple.get_apple_pos(), 5)  #TODO: apple circle

        score_font = font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 120, 10)
        screen.blit(score_font, score_rect)

        b_score_font = font.render(f'Best-Score: {best_score}', True, (255, 255, 255))
        b_score_rect = b_score_font.get_rect()
        b_score_rect.topleft = (40, 10)
        screen.blit(b_score_font, b_score_rect)

        snake.print_snake(screen)
        
        if dead_line:
            if score > best_score:
                with open(os.path.join(dir_name, 'best_score.txt'), 'w') as r:
                    r.write(str(score))
            pygame.mixer.music.stop()
            break

        pygame.display.update()

    
    game_over = Fonts("Game Over", "Pixeled", 50, (600 // 2, 20), (255, 26, 26))
    game_over.print_font(screen)
    pygame.display.update()
    pygame.mixer.Sound.play(pygame.mixer.Sound("GameSounds/game-over.ogg"))
    pygame.time.wait(2000)
        # menu()

