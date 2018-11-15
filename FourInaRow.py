import sys, pygame, numpy, math, random
from pygame.locals import *

pygame.init()
width = 700
height = 700

size = (width, height)

screen = pygame.display.set_mode(size)

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SquareSize = 100
RADIUS = int(SquareSize/2 - 5)
WIDTH = 800
HEIGHT = 800
turn = 0

pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer.music.load('bensound-funkyelement.mp3')
# pygame.mixer.volume_set(3)
pygame.mixer.music.play(-1)

def createboard():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT)) # (ROW_COUNT, ROW_COUNT)
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def validLocation(board, col):
    return board[ROW_COUNT-1][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(numpy.flip(board, 0))

def winningMove(board, piece):
    print(board)
            # all winning moves for horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

            # all winning moves for vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

            # all winning moves for positive slope diagonals
    for c in range(COLUMN_COUNT - 3):
         for r in range(ROW_COUNT - 3):
             if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+2] == piece:
                return True

            # all winning moves for negative slope diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def drawBoard(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SquareSize, r*SquareSize+SquareSize, SquareSize, SquareSize))
            pygame.draw.circle(screen, BLACK, (int(c*SquareSize + SquareSize/2), int(r*SquareSize + SquareSize + SquareSize/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SquareSize + SquareSize / 2), height - int(r * SquareSize + SquareSize / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SquareSize + SquareSize / 2), height - int(r * SquareSize + SquareSize / 2)), RADIUS)
    pygame.display.update()



board = createboard()
printBoard(board)
drawBoard(board)
pygame.font.init()
myFont = pygame.font.SysFont("monospace", 75)
game_over = False
width = COLUMN_COUNT + SquareSize
height = (ROW_COUNT+1) + SquareSize
size = (width, height)

pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SquareSize))
            posx = event.posx[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SquareSize/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SquareSize/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SquareSize))
            posx = event.posx[0]
            # print(event.pos)
            if turn == 0:
                col = int(math.floor(posx/SquareSize))

                if validLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 1)

                    if winningMove(board, 1):
                        label = myFont.render("Player 1 Wins!!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            else:
                posx = event.posx[0]
                col = int(math.floor(posx/SquareSize))

                if validLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 2)

                    if winningMove(board, 2):
                        label = myFont.render("Player 2 Wins!!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            if game_over == True:
                pygame.mixer.music.load('bensound-clapandyell.mp3')
                pygame.mixer.volume_set(0.5)
                pygame.mixer.music.play(-1)
                confetti = pygame.image.load('confetti.png').convert()
                Confetti = pygame.image.get_rect()


                class ConfettiDrop(object):
                    def move(self, x, y):
                        self.confetti.center[0] += x
                        self.confetti.center[1] += y


                screen.blit(confetti, (0, 0))
                pygame.display.update()
                # load up confetti sprite and make it fall down the screen

            printBoard(board)
            drawBoard(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(10000)