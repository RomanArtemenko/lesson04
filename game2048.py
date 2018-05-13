import pygame
import time
from core import game as g

CELL_WIDTH = 106
BORDER_WIDTH = 15


FONT_COLOR = (74, 58, 58)
EMPTY_CELL = (243, 221, 221)
BOARD = (237, 145, 33)
GAME_OVER = (255,0,0)

CELL_COLOR = {0: (181, 184,	177),
2: (243, 221, 221),
4: (251, 206, 177),
8: (205, 149, 117),
16: (255, 223, 132),
32: (205, 127,50),
64: (213, 113, 63),
128: (255, 207, 72),
256: (169, 29, 17),
512: (195, 77, 10),
1024: (243, 71, 35),
2048: (255, 215, 0)}

def main():
    game = g.Game(4)

    pygame.init()

    pygame.display.set_caption("2048")

    screen = pygame.display.set_mode((500,550))
    screen.fill((127, 102, 102))

    game_font = pygame.font.SysFont("Terminal", 40)

    running = True
 
    while running:
        for row in range(game.width):
            for col in range(game.width):
                pygame.draw.rect(screen,
                    CELL_COLOR[game.get_field()[row][col]],
                    ((BORDER_WIDTH + (col * (BORDER_WIDTH + CELL_WIDTH))), 
                    (BORDER_WIDTH + (row * (BORDER_WIDTH + CELL_WIDTH))), 
                    CELL_WIDTH, CELL_WIDTH))

                if game.get_field()[row][col] != game.EMPTY_CELL:
                    text = game_font.render(str(game.get_field()[row][col]), True, FONT_COLOR)
                    text_rect = text.get_rect(center=((BORDER_WIDTH + (col * (BORDER_WIDTH + CELL_WIDTH))) + (CELL_WIDTH/2),
                     (BORDER_WIDTH + (row * (BORDER_WIDTH + CELL_WIDTH))) + (CELL_WIDTH/2)))
                    screen.blit(text, text_rect)    


        pygame.draw.rect(screen,
                    BOARD,
                    (0, 500, 500, 50))        

        text_score = game_font.render("Score : " + str(game.get_score()), True, FONT_COLOR)
        screen.blit(text_score, text_score.get_rect(center=(250, 525)))            
        
        pygame.display.update()

        if not game.has_moves():
            text_game_over = game_font.render("GAME OVER", True, GAME_OVER)
            screen.blit(text_game_over, text_game_over.get_rect(center=(250, 250))) 

            running = False  
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    game.move_down()
                elif event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_UP:
                    game.move_up()

        time.sleep(0.02)

if __name__ ==  '__main__':
    main()