import pygame as pg
import sys
from Game import *


def main():
    pg.init()
    game = Game()
    game_over = False

    game.createboard()
    game.draw_grid()
    human, ai = 1, 2
    player = human
    # gameloop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseX) // 200
                clicked_col = int(mouseY) // 200

                if game.available_square(clicked_row, clicked_col):
                    if player == human:
                        game.HUMAN(clicked_row, clicked_col)
                        if game.check_win(player):
                            game_over = True
                            print("Player YOU win!!")
                        player = ai
                    elif player == ai:
                        game.AI()
                        if game.check_win(player):
                            game_over = True
                            print("AI wins!!")
                        player = human
                    pg.display.update()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_y:
                    game.restart()
        pg.display.update()


if __name__ == "__main__":
    main()
