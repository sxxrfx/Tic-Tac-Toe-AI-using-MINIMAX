import pygame as pg
import numpy as np
import math
# import itertools
# import random


class Game:
    def __init__(self):
        self.BG_COLOR = (240, 240, 240)
        self.WIDTH = 600
        self.HEIGHT = 600
        self.LN_COLOR = (100, 100, 100)
        self.W1_COLOR = (20, 50, 200)
        self.W2_COLOR = (200, 50, 20)
        self.COLS = 3
        self.ROWS = 3
        global ai
        global human
        ai = 2
        human = 1
        # self.l = (1, 2)
        # random.shuffle(l)
        # ai, player = self.l
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        global board
        board = np.zeros((self.ROWS, self.COLS))
        self.icon = pg.image.load(".\\images\\icon.png")
        self.x = pg.image.load(".\\images\\x.png")
        self.o = pg.image.load(".\\images\\o.png")
        self.intro = pg.image.load(".\\images\\intro.png")
        self.intro = pg.transform.scale(self.intro, (self.WIDTH, self.HEIGHT))
        self.x = pg.transform.scale(
            self.x, (int(self.WIDTH/3), int(self.HEIGHT/3)))
        self.o = pg.transform.scale(
            self.o, (int(self.WIDTH/3-30), int(self.HEIGHT/3-30)))

    # drawing grid lines
    def draw_grid(self):
        pg.draw.line(self.screen, self.self.LN_COLOR,
                     (20, 200), (580, 200), 20)
        pg.draw.line(self.screen, self.self.LN_COLOR,
                     (20, 400), (580, 400), 20)
        pg.draw.line(self.screen, self.self.LN_COLOR,
                     (200, 20), (200, 580), 20)
        pg.draw.line(self.screen, self.self.LN_COLOR,
                     (400, 20), (400, 580), 20)

    def createboard(self):
        # Title and Icon
        pg.display.set_caption("Tic-Tac-Toe")
        pg.display.set_icon(self.icon)
        self.screen.fill(self.BG_COLOR)

    def mark_square(self, row, col, player):
        if self.available_square(row, col):
            board[row][col] = player
        else:
            print("NOT Available")

# checking if board full

    def is_full(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == 0:
                    return False
        return True

    # drawing grid lines

    def draw_grid(self):
        pg.draw.line(self.screen, self.LN_COLOR, (20, 200), (580, 200), 20)
        pg.draw.line(self.screen, self.LN_COLOR, (20, 400), (580, 400), 20)
        pg.draw.line(self.screen, self.LN_COLOR, (200, 20), (200, 580), 20)
        pg.draw.line(self.screen, self.LN_COLOR, (400, 20), (400, 580), 20)

    # drawing x or o

    def draw_figure(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == 1:
                    self.screen.blit(self.x, ((row*200), (col*200)))
                if board[row][col] == 2:
                    self.screen.blit(self.o, ((row*200+16), (col*200+16)))

    def draw_rwin(self, col, player):
        if player == 1:
            pg.draw.line(self.screen, self.W1_COLOR, (70, col*200+100),
                         (530, col*200+100), 30)
        else:
            pg.draw.line(self.screen, self.W2_COLOR, (70, col*200+100),
                         (530, col*200+100), 30)

    def draw_cwin(self, row, player):
        if player == 1:
            pg.draw.line(self.screen, self.W1_COLOR,
                         (row*200+100, 70), (row*200+100, 530), 30)
        else:
            pg.draw.line(self.screen, self.W2_COLOR, (row*200+100, 70),
                         (row*200+100, 530), 30)

    def draw_d1win(self, player):
        if player == 1:
            pg.draw.line(self.screen, self.W1_COLOR, (30, 30),
                         (570, 570), 30)
        else:
            pg.draw.line(self.screen, self.W2_COLOR, (30, 30),
                         (570, 570), 30)

    def draw_d2win(self, player):
        if player == 1:
            pg.draw.line(self.screen, self.W1_COLOR, (570, 30),
                         (30, 570), 30)
        else:
            pg.draw.line(self.screen, self.W2_COLOR, (570, 30),
                         (30, 570), 30)

    def eval(self):
        b = board.copy()
        for row in range(self.ROWS):
            if ((b[row][0] == b[row][1]) and (b[row][1]
                                              == b[row][2])):
                if(b[row][0] == human):
                    return 10
                elif(b[row][0] == ai):
                    return (-10)

        for col in range(self.COLS):
            if((b[0][col] == b[1][col]) and (b[1][col]
                                             == b[2][col])):
                if(b[0][col] == human):
                    return 10
                elif(b[0][col] == ai):
                    return (-10)

        if((b[0][0] == b[1][1]) and (b[1][1] == b[2][2])):
            if(b[1][1] == human):
                return 10
            elif(b[1][1] == ai):
                return (-10)

        if((b[2][0] == b[1][1]) and (b[1][1] == b[0][2])):
            if(b[1][1] == human):
                return 10
            elif(b[1][1] == ai):
                return (-10)
        if self.is_full():
            return 0
        return -1

    def restart(self):
        self.screen.fill(self.BG_COLOR)
        self.draw_grid()
        game_over = False
        player = 1
        for row in range(self.ROWS):
            for col in range(self.COLS):
                board[row][col] = 0

    def minimax(self, Max, depth, alpha, beta):
        score = self.eval()
        if(score != -1):
            return score
        if(Max):
            bestEval = -math.inf
            for row in range(3):
                for col in range(3):
                    if (board[row][col] == 0):
                        board[row][col] = human
                        val = self.minimax(not Max, depth+1, alpha, beta)
                        board[row][col] = 0
                        bestEval = max(bestEval, val)
                        alpha = max(bestEval, alpha)
                        if beta <= alpha:
                            return alpha-depth
            return alpha-depth
        else:
            best = math.inf
            for row in range(3):
                for col in range(3):
                    if (board[row][col] == 0):
                        board[row][col] = ai
                        val = self.minimax(not Max, depth+1, alpha, beta)
                        board[row][col] = 0
                        best = min(best, val)
                        beta = min(best, beta)
                        if beta <= alpha:
                            return beta+depth
            return beta+depth

    def findnext(self):
        bestnow = math.inf
        bestmove = [-1, -1]
        for row in range(3):
            for col in range(3):
                if (board[row][col] == 0):
                    board[row][col] = ai
                    moveval = self.minimax(True, 1, -math.inf, math.inf)
                    board[row][col] = 0
                    if(moveval < bestnow):
                        bestnow = moveval
                        bestmove = [row, col]
        return bestmove

    def AI(self):
        row, col = self.findnext()
        self.mark_square(row, col, ai)
        print("ai's move")
        print(board)
        self.draw_figure()

    def HUMAN(self, row, col):
        self.mark_square(row, col, human)
        print("Your move")
        print(board)
        self.draw_figure()

    def check_win(self, player):
        for row in range(self.ROWS):
            if ((board[row][0] == board[row][1]) and (board[row][1]
                                                      == board[row][2]) and (board[row][1] == player)):
                self.draw_cwin(row, player)
                return True

        for col in range(self.COLS):
            if((board[0][col] == board[1][col]) and (board[1][col]
                                                     == board[2][col]) and (board[1][col] == player)):
                self.draw_rwin(col, player)
                return True

        if((board[0][0] == board[1][1]) and (board[1][1] == board[2][2])
           and (board[1][1] == player)):
            self.draw_d1win(player)
            return True

        if((board[2][0] == board[1][1]) and (board[1][1] == board[0][2])
           and (board[1][1] == player)):
            self.draw_d2win(player)
            return True
        return False

# available sqaure on the board

    def available_square(self, row, col):
        return board[row][col] == 0
