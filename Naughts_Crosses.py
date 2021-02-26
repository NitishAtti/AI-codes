from numpy import *

class play_Board:
    def __init__(self,setup = array([" "," "," "," "," "," "," "," "," "]).reshape(3,3)):
        self.setup = setup

    def valid_move(self):
        valid = []
        for i in range(3):
            for j in range(3):
                if self.setup[i][j] == " ":
                    valid.append((i,j))
        return valid

    def Game_over(self):
        if self.win() == "X":
            print("O losses the game and the winner is X")
            return True
        elif self.win() == "O":
            print("X losses the game and the winner is O")
            return True
        elif self.win() == "Tie":
            print("the game is tied")
            return True
        elif len(self.valid_move()) == 0:
            return True
        return False

    def win(self):
        if self.setup[0][0] + self.setup[0][1] + self.setup[0][2] in ["OOO","XXX"]:
            a = self.setup[0][0]
            return a
        elif self.setup[1][0] + self.setup[1][1] + self.setup[1][2] in ["OOO","XXX"]:
            a = self.setup[1][0]
            return a
        elif self.setup[2][0] + self.setup[2][1] + self.setup[2][2] in ["OOO", "XXX"]:
            a = self.setup[2][0]
            return a
        elif self.setup[0][0] + self.setup[1][1] + self.setup[2][2] in ["OOO", "XXX"]:
            a = self.setup[0][0]
            return a
        elif self.setup[0][0] + self.setup[1][0] + self.setup[2][0] in ["OOO","XXX"]:
            a = self.setup[0][0]
            return a
        elif self.setup[0][1] + self.setup[1][1] + self.setup[2][1] in ["OOO", "XXX"]:
            a = self.setup[0][1]
            return a
        elif self.setup[0][2] + self.setup[1][2] + self.setup[2][2] in ["OOO", "XXX"]:
            a = self.setup[0][2]
            return a
        elif self.setup[0][2] + self.setup[1][1] + self.setup[2][0] in ["OOO", "XXX"]:
            a = self.setup[0][2]
            return a
        elif len(self.valid_move()) == 0:
            a = "Tie"
            return a
        else:
            return None

    def minimax(self,symbol,depth = 0):
        if symbol == "X":
            enemy = "O"
            points = 100
        else:
            enemy = "X"
            points = -100
        if self.Game_over():
            if self.win() == "X":
                return points + depth, None
            elif self.win() == "O":
                return points - depth, None
            elif self.win() == "Tie":
                return 0, None

        for move in self.valid_move():
            self.setup[move[0]][move[1]] = symbol
            cost, _ = self.minimax(enemy,depth+1)
            self.setup[move[0]][move[1]] = " "
            if symbol == "O":
                if cost > points:
                    points, bestmove = cost, move
            else:
                if cost < points:
                    points, bestmove = cost, move
        return points,bestmove

start = play_Board()
print(" Welcome to Tic -Tac Toe or Naughts and Crosses( 3x3) ")
print("Press X or O , to play this game")
symbol = input()
if symbol == "X":
    for i in range(9):
        print("enter row and col for your move")
        row,col = (input().split())
        row = int(row)
        col = int(col)
        if start.setup[row][col] == " ":
            start.setup[row][col] = "X"
            print(start.setup)
        if start.Game_over():
            break
        print(start.minimax(symbol))
        print("enter row and col for your move")
        row, col = (input().split())
        row = int(row)
        col = int(col)
        if start.setup[row][col] == " ":
            start.setup[row][col] = "O"
            print(start.setup)
        if start.Game_over():
            break
elif symbol == "O":
    row = random.randint(0,2)
    col = random.randint(0,2)
    start.setup[row][col] = "X"
    print(start.setup)
    for i in range(9):
        print("enter row and col for your move")
        row, col = (input().split())
        row = int(row)
        col = int(col)
        if start.setup[row][col] == " ":
            start.setup[row][col] = "O"
            print(start.setup)
        if start.Game_over():
            break
        print(start.minimax("X"))
        print("enter row and col for your move")
        row, col = (input().split())
        row = int(row)
        col = int(col)
        if start.setup[row][col] == " ":
            start.setup[row][col] = "X"
            print(start.setup)
        if start.Game_over():
            break
