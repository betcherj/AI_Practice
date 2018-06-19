#Jack Betcher
#Minimax
import random

computerLetter = 'O'
playerLetter = 'X'
#draws board
def drawBoard(board):
    print('' + board[0] + '|' + board[1] + '|' + board[2])
    print('-------')
    print('' + board[3] + '|' + board[4] + '|' + board[5])
    print('-------')
    print('' + board[6] + '|' + board[7] + '|' + board[8])


def whoGoesFirst():
    if random.choice([0,1])==1:
        return 'Player'
    else:
        return 'Computer'

def playAgain():
    print('Do you want to play again')
    return raw_input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

#checks if board has a winner 
def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))

def isSpaceFree(board, move):
    return board[move] == ''

#gets and returns the players move 
def getPlayerMove(board):
    move = '' 
    while move not in '0 1 2 3 4 5 6 7 8'.split() or not isSpaceFree(board, int(move)):
        print('what is your next move? (0,1,2,3,4,5,6,7,8)')
        move = str(input())
    return int(move)

 
def checkMovesList(board, movesList):
    possibleMoves = list()
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) == 0:
        return None
    else:
        return possibleMoves
    

#checks if the board is full 
def isBoardFull(board):
    for i in range(len(board)):
        if isSpaceFree(board,i):
            return False
    return True 

def evaluate(board):
    if isBoardFull(board):
        if isWinner(board, computerLetter):
            return 10
        elif isWinner(board, playerLetter):
            return -10
    else:
        return 0

print('Unbeatable TicTacToe')

def getBestMove(board):
    bestMove = None
    avail = checkMovesList(board, [0,1,2,3,4,5,6,7,8])
    depth = len(avail)
    bestVal = -1000
    for i in avail:
        makeMove(board, computerLetter, i)
        val = miniMax(board, depth+1, False)
        makeMove(board, '', i)
        print 'val is:', val
        if val>bestVal:
            bestVal = val
            bestMove = i
            print 'best move is: ', bestMove
    return bestMove   

def miniMax(board, depth, isMax):
    score = evaluate(board)
    if score == 10:
        return score
    if score == -10:
        return score 
    avail = checkMovesList(board, [0,1,2,3,4,5,6,7,8])
    if isBoardFull(board):
        return 0
    if isMax:
        bestVal = -100000
        for i in avail:
            makeMove(board, computerLetter, i)
            val = miniMax(board, depth+1, False)
            bestVal = max(bestVal, val)
            makeMove(board, '', i)
        return bestVal
    else:
        bestVal = 100000
        for i in avail:
            makeMove(board, playerLetter, i)
            val = miniMax(board, depth+1, True)
            bestVal = min(bestVal, val)
            makeMove(board, '', i)
        return bestVal
    
while True:
    board = ['']*9
    turn = whoGoesFirst()
    print(turn + ' goes first')
    stillPlaying = True
    while stillPlaying:
        drawBoard(board)
        if turn == 'Computer':
            move = getBestMove(board)
            makeMove(board, computerLetter, move)
            turn = 'Player'
        else:
            move = getPlayerMove(board)
            makeMove(board, playerLetter, move)
            turn = 'Computer'
        print turn
        if isWinner(board, computerLetter):
            print('Computer Wins')
            drawBoard(board)
            stillPlaying = False
        elif isWinner(board, playerLetter):
            print('Player Wins')
            drawBoard(board)
            stillPlaying = False
        elif isBoardFull(board):
            print('Tie')
            drawBoard(board)
            stillPlaying = False
    if not playAgain():
        break




    
