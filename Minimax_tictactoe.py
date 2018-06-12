<<<<<<< Updated upstream
#Jack Betcher
#Minimax
import random

#draws board
def drawBoard(board):
    print('' + board[0] + '|' + board[1] + '|' + board[2])
    print('-------')
    print('' + board[3] + '|' + board[4] + '|' + board[5])
    print('-------')
    print('' + board[6] + '|' + board[7] + '|' + board[8])


def inputPlayerLetter():
    letter = ''
    while(letter == ''):
        letter = raw_input("X's or O's\n")
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

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

#Checks if moves in a list are availble and chooses one randomly 
def checkMovesList(board, movesList):
    possibleMoves = list()
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) == 0:
        return None
    else:
        return possibleMoves
    
#returns the Computers Move 
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #checks to see if the computer can win this turn 
    for i in range (len(board)):
        copy = board[:]
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #checks to see if the player can win next turn and blocks
    for i in range (len(board)):
        copy = board [:]
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    #plays in a corner if avalible
    move = random.choice(checkMovesList(board, [0,2,6,9]))
    if move != None:
        return move
    #plays in the center if available
    if isSpaceFree(board, 4):
        return 4

    #move on one of the sides
    return random.choice(checkMovesList(board, [1,3,5,7]))
#checks if the board is full 
def isBoardFull(board):
    for i in range(len(board)):
        if isSpaceFree(board,i):
            return False
    return True 

print('Unbeatable TicTacToe')


def miniMax(board, letter):
    moves = checkMovesList(board, [0,1,2,3,4,5,6,7,8])
    if isWinner(board, playerLetter):
        return -10
    elif isWinner(board, computerLetter):
        return 10
    elif len(moves)==0:
        return 0
    board[moves[i]] = letter
    if letter == computerLetter:
        result = miniMax(board,playerLetter)
        moves[i] = result
    else:
        result = miniMax(board, computerLetter)
        moves[i] = result

    moves.append[move]
                        
        
    









    
=======
#Jack Betcher
#Minimax
import random

#draws board
def drawBoard(board):
    print('' + board[0] + '|' + board[1] + '|' + board[2])
    print('-------')
    print('' + board[3] + '|' + board[4] + '|' + board[5])
    print('-------')
    print('' + board[6] + '|' + board[7] + '|' + board[8])


def inputPlayerLetter():
    letter = ''
    while(letter == ''):
        letter = raw_input("X's or O's\n")
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

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

#Checks if moves in a list are availble and chooses one randomly 
def checkMovesList(board, movesList):
    possibleMoves = list()
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) == 0:
        return None
    else:
        return possibleMoves
    
#returns the Computers Move 
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #checks to see if the computer can win this turn 
    for i in range (len(board)):
        copy = board[:]
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #checks to see if the player can win next turn and blocks
    for i in range (len(board)):
        copy = board [:]
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    #plays in a corner if avalible
    move = random.choice(checkMovesList(board, [0,2,6,9]))
    if move != None:
        return move
    #plays in the center if available
    if isSpaceFree(board, 4):
        return 4

    #move on one of the sides
    return random.choice(checkMovesList(board, [1,3,5,7]))
#checks if the board is full 
def isBoardFull(board):
    for i in range(len(board)):
        if isSpaceFree(board,i):
            return False
    return True 

print('Unbeatable TicTacToe')


def miniMax(board, letter):
    avail = checkMovesList(board, [0,1,2,3,4,5,6,7,8])
    if isWinner(board, playerLetter):
        return -10
    elif isWinner(board, computerLetter):
        return 10
    elif len(avail)==0:
        return 0
    moves = []
    for i in avail:
        move = []
        move.append((board[i],))
        board[i]=letter
        if letter == computerLetter:
            result = miniMax(board,playerLetter)
            move[i][1] = result
        else:
            result = miniMax(board, computerLetter)
            move[i][1] = result
        board[i] = move[i][0]
        moves.append[move]
    bestMove=list((,))
    
    
        
    









    
>>>>>>> Stashed changes
