from asyncio import Event
from copyreg import dispatch_table
from operator import truediv
from pickle import TRUE
import numpy as np
import pygame as pg
import sys
import time
from pygame.locals import *

pg.init()


class tic_tac_toe:
    p1 = True
    win = False
    tie = False
    board = [[None]*3, [None]*3, [None]*3]


class display(tic_tac_toe):
    def __init__(self):
        self.x_img = pg.image.load("x_tic.png")
        self.o_img = pg.image.load("o_tic.png")
        self.x_img = pg.transform.scale(self.x_img, (150, 150))
        self.o_img = pg.transform.scale(self.o_img, (150, 150))
        self.width = 600
        self.height = 600
        self.dis = pg.display.set_mode((self.width, self.height + 200), 0, 32)
        self.dis.fill((255, 255, 255))

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    return False
        tic_tac_toe.tie = True
        return True

    def check_win(self):
        red = (255, 64, 64)
        if tic_tac_toe.p1:
            check = 'X'
        else:
            check = 'O'

        if self.board[0][0] == self.board[0][1] == self.board[0][2] == check:
            pg.draw.line(self.dis, red, start_pos=(0, self.height/6),
                         end_pos=(self.width, self.height/6), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == check:
            pg.draw.line(self.dis, red, start_pos=(0, self.height/2),
                         end_pos=(self.width, self.height/2), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == check:
            pg.draw.line(self.dis, red,  start_pos=(0, 5 * self.height/6),
                         end_pos=(self.width, 5 * self.height/6), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == check:
            pg.draw.line(self.dis, red, start_pos=(self.width/6, 0),
                         end_pos=(self.width/6, 5 * self.height), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == check:
            pg.draw.line(self.dis, red, start_pos=(self.width/2, 0),
                         end_pos=(self.width/2, 5 * self.height), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == check:
            pg.draw.line(self.dis, red, start_pos=(5 * self.width/6, 0),
                         end_pos=(5 * self.width/6, 5 * self.height), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == check:
            pg.draw.line(self.dis, red, start_pos=(0, 0),
                         end_pos=(self.width, self.height), width=9)
            tic_tac_toe.win = True
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == check:
            pg.draw.line(self.dis, red, start_pos=(
                self.width, 0), end_pos=(0, self.height), width=9)
            tic_tac_toe.win = True
            return True

        tic_tac_toe.p1 = not tic_tac_toe.p1
        return False

    def reset_game(self):
        replay = pg.image.load("PlayAgainButton.png")
        replay = pg.transform.scale(replay, (400, 196))
        self.dis.blit(replay, (100, 200))

        while (True):
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pg.mouse.get_pos()
                        if x >= 100 and x <= 500 and y >= 202 and y <= 398:
                            return True

    def display_game(self):

        self.dis.fill((255, 255, 255), rect=(0, 0, 600, 600))
        self.dis.fill((0, 0, 0), rect=(0, 600, 600, 300))
        tic_tac_toe.win = False

        black = (0, 0, 0)
        pg.draw.line(self.dis, color=black, start_pos=(self.width / 3, 0),
                     end_pos=(self.width / 3, self.height), width=9)
        pg.draw.line(self.dis, color=black, start_pos=(2 * self.width / 3, 0),
                     end_pos=(2 * self.width / 3, self.height), width=9)
        pg.draw.line(self.dis, color=black, start_pos=(0, self.height/3),
                     end_pos=(self.width, self.height/3), width=9)
        pg.draw.line(self.dis, color=black, start_pos=(0, 2 * self.height/3),
                     end_pos=(self.width, 2 * self.height/3), width=9)

        #self.dis.fill((0, 0, 0), (900, 600, 0, 600))

        pg.display.update()

    def init_window(self):
        init_img = pg.image.load("unnamed.png")
        init_img = pg.transform.scale(init_img, (600, 600))
        self.dis.blit(init_img, (0, 0))
        self.dis.fill((0, 0, 0), rect=(0, 600, 600, 300))
        pg.display.update()

    def update_status(self):
        self.dis.fill((0, 0, 0), rect=(0, 600, 600, 300))
        text = pg.font.Font(None, 32)

        if tic_tac_toe.tie:
            status = "Tie"
            text = text.render(status, False, (255, 0, 0))
            self.dis.blit(text, (273, 675))
            return
        elif tic_tac_toe.p1 and not tic_tac_toe.win:
            status = "Player 1's Turn"
        elif not tic_tac_toe.p1 and not tic_tac_toe.win:
            status = "Player 2's Turn"
        elif tic_tac_toe.p1:
            status = "Player 1 Won!"
        else:
            status = "Player 2 Won!"

        text = text.render(status, False, (255, 0, 0))
        self.dis.blit(text, (210, 675))

    def update_dis(self, x, y):
        row = 0
        col = 0
        xpos = 0
        ypos = 0

        if y < self.height/3:
            row = 1
            ypos = 25
        elif y < 2 * self.height/3:
            row = 2
            ypos = 225
        else:
            ypos = 425
            row = 3

        if x < self.width/3:
            xpos = 25
            col = 1
        elif x < 2 * self.width/3:
            xpos = 225
            col = 2
        else:
            xpos = 425
            col = 3

        if tic_tac_toe.board[row - 1][col - 1] != None:
            return

        if tic_tac_toe.p1:
            self.dis.blit(self.x_img, (xpos, ypos))
            tic_tac_toe.board[row - 1][col - 1] = 'X'
        else:
            self.dis.blit(self.o_img, (xpos, ypos))
            tic_tac_toe.board[row - 1][col - 1] = 'O'

        pg.display.update()


game = tic_tac_toe()
game_dis = display()
game_dis.init_window()
pg.event.pump()
pg.time.wait(3000)
game_dis.display_game()
play = True
while (play):
    game_dis.update_status()
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pg.mouse.get_pos()
                game_dis.update_dis(x, y)
                if game_dis.check_win() or game_dis.check_tie():
                    game_dis.update_status()
                    if game_dis.reset_game():
                        game_dis.display_game()
                        tic_tac_toe.p1 = True
                        tic_tac_toe.tie = False
                        tic_tac_toe.board = [[None]*3, [None]*3, [None]*3]
