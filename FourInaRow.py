import sys, pygame, numpy

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
#Global variables define what something means

def createboard():
    board = numpy.zeros((ROW_COUNT, ROW_COUNT))
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
            # all winning moves for horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

            # all winning moves for vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r+3][c] == piece:
                return True

            # all winning moves for positive slope diagonals
    for c in range(COLUMN_COUNT - 3):
         for r in range(ROW_COUNT - 3):
             if board[r][c] == piece and board[r + 1][c+1] == piece and board[r + 2][c+2] == piece and board[r + 3][c+2] == piece:
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
            pygame.draw.circle(screen, BLACK)

board = createboard()
printBoard(board)
game_over = False
turn = 0

pygame.init()

SquareSize = 100

width = COLUMN_COUNT + SquareSize
height = (ROW_COUNT+1) + SquareSize
size = (width, height)
screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue
            # if turn == 0:
            #     col = int(input("Give yourself a name, player 1 (0, 6):"))
            #
            #     if validLocation(board, col):
            #         row = getNextOpenRow(board, col)
            #         dropPiece(board, row, col, 1)
            #
            #         if winningMove(board, 1):
            #             print("Player 1 Wins!")
            #             game_over = True
            #     # print(selection)
            #     # print(type(selection))
            #     # possibly take out the int
            # else:
            #     col = int(input("Give yourself a name, player 2 (0, 6):"))
            #
            #     if validLocation(board, col):
            #         row = getNextOpenRow(board, col)
            #         dropPiece(board, row, col, 2)
            #
            #         if winningMove(board, 2):
            #             print("Player 2 Wins!")
            #             game_over = True
            #     # print(selection)
            #     # print(type(selection))
            #     # possibly take out the int
            #     # print(board)
            #
            # printBoard(board)
            #
            # turn += 1
            # turn = turn % 2
