from random import randint
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
winner = None
gameRunning = True



def gameboard_show(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
# gameboard_show(board)




def PlayerInput(board):
    i = int(input("Enter a number 1-9: "))
    if i  >= 1 and i <= 9 and board[i-1] == "-":
        board[i-1] = current_player 
    else:
        print("Player already there in that spot.")

def horizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[5] == board[6] == board[7] and board[6] != "-":
        winner = board[5]
        return True
    

def row(board):
    global winner
    if board[0] == board[3] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True  
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def dia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    if "-" not in board:
        gameboard_show(board)
        print("====TIE=====")
        gameRunning=False

def switchplayer():
    global current_player
    if current_player == "X":
        current_player="O"
    else:
        current_player="X"

def check_win():
    if horizontle(board) or row(board) or dia(board):
        if winner == "0":
           print("The winner is Computer.")
        else:
           print("The winner is You.")

def computer(board):
     while current_player == "O":
         position = randint(0,8)
         if board[position] == "-":
             board[position]="O"
             switchplayer()


while gameRunning:
    gameboard_show(board)
    PlayerInput(board)
    check_win()
    check_tie(board)
    switchplayer()
    computer(board)

