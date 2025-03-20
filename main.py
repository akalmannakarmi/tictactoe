import random
import copy

class TickTackToe:
    board = [
        ["","",""],
        ["","",""],
        ["","",""],
    ]
    last_player = "X"

    def place(self,x,y,value):
        if value != "X" and value != "O":
            raise ValueError("Invalid Value")
        if self.last_player == value:
            raise ValueError("Not Your Turn")
        
        if x not in [0,1,2] or y not in [0,1,2]:
            raise ValueError("Invalid position")
        if self.board[x][y]:
            raise ValueError("Position Taken")
        
        self.last_player=value
        self.board[x][y]=value
    
    def check(self):
        wins = [
            self.board[0][0] + self.board[0][1] + self.board[0][2],
            self.board[1][0] + self.board[1][1] + self.board[1][2],
            self.board[2][0] + self.board[2][1] + self.board[2][2],
            self.board[0][0] + self.board[1][0] + self.board[2][0],
            self.board[0][1] + self.board[1][1] + self.board[2][1],
            self.board[0][2] + self.board[1][2] + self.board[2][2],
            self.board[0][0] + self.board[1][1] + self.board[2][2],
            self.board[0][2] + self.board[1][1] + self.board[2][0],
        ]
        for value in wins:
            if len(value)!=3:
                break
        else:
            print("Draw!")
            return True

        if "XXX" in wins:
            print("X Won!")
            return True
        if "OOO" in wins:
            print("O Won!")
            return True
        return False

    def get_map(self):
        return copy.deepcopy(self.board)

def run():
    game = TickTackToe()
    
    while True:
        # Picking random place
        while True:
            try:
                randX = random.randint(0,2)
                randY = random.randint(0,2)
                game.place(randX,randY,"O")
                break
            except ValueError:
                pass
        
        if game.check():
            break

        # printing the map
        map = game.get_map()
        for i in range(3):
            for j in range(3):
                print(map[i][j] or " " ,end=" " if j==2 else "|")
            print("\n------"if  i!=2 else "")
        print()

        while True:
            try:
                x = int(input("Enter pos X:"))
                y = int(input("Enter pos Y:"))
                break
            except ValueError:
                print("Try again Invalid Position!")
    
        game.place(x,y,"X")

        if game.check():
            break

    map = game.get_map()
    for i in range(3):
        for j in range(3):
            print(map[i][j] or " " ,end=" " if j==2 else "|")
        print("\n------"if  i!=2 else "")
    print()

if __name__ == "__main__":
    run()
