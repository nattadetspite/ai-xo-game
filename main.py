
# game design
'''
game design
- create board
- create game win condition
- check valid move
- create agent using basic algorithm
'''
from random import randint
board = [''] * 9


def printBoard(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

# 1 : 2


def winCondition(player):
    # across
    across = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # down
    down = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # diagonal
    diagonal = [[1, 5, 9], [3, 5, 7]]

    countAcross = [0, 0, 0]
    countDown = [0, 0, 0]
    countDiagonal = [0, 0, 0]
    for item in player:
        # check across
        for i in range(len(across)):
            if item in across[i]:
                countAcross[i] += 1
        # check down
        for i in range(len(down)):
            if item in down[i]:
                countDown[i] += 1
        # checkd diagonal
        for i in range(len(diagonal)):
            if item in diagonal[i]:
                countDiagonal[i] += 1
    if 3 in countAcross:
        return True
    elif 3 in countDown:
        return True
    elif 3 in countDiagonal:
        return True
    else:
        return False


def agentPlay(player, board):
    # check valide move
    validmove = []
    for i in range(len(board)):
        if len(board[i]) == 0:
            validmove.append(i)

    result = randint(0, len(validmove) - 1)
    return validmove[result]


def main():
    print('main start')

    printBoard(board)
    player1 = []
    player2 = []
    # 1 = x , 2 = o
    turn = 0
    while True:
        if(turn >= 9):
            print('board is full.')
            return
        if(turn % 2 == 0):
            player = player1
            opponent = player2
            isAgent = False
            name = 'x'
        else:
            player = player2
            opponent = player1
            isAgent = True
            name = 'o'

        if isAgent:
            print('-------------------')
            agentposition = agentPlay(player, board)

            board[int(agentposition) - 1] = name
            player.append(int(agentposition))
            printBoard(board)
            turn += 1
        else:
            while True:
                print(name + ' where do you want to play')
                play = input()
                if int(play) in opponent or int(play) in player:
                    print('move is invalid')
                    pass
                else:
                    board[int(play) - 1] = name
                    player.append(int(play))
                    printBoard(board)
                    turn += 1
                    break
        # check win
        if winCondition(player):
            print('player ' + name + ' win')
            break


if __name__ == "__main__":
    main()
