#### Boggle Solver Main ####
#### By Thomas Back     ####
#### 1/24/2018 CS470    ####

import time

class boggleSolver:
    
    def __init__(self):
        self.board = []

    #loads NxN board into matrix
    def loadBoard(self, boardFile):
        #temp array
        temp = []
        count = 0

        board = open(boardFile)
        board = board.read()
        board.strip(' ')

        #for loop to loop through letters, disregards white space
        for letter in range(len(board)):

            #if reached new line, save that dimension within array
            if board[letter] == '\n':
                self.board[-1] = temp
                temp = []
                count = 0
                
            #if blank space, skip
            elif board[letter] == " ":
                continue
            

            else :
                temp[count] = board[letter]
                count += 1
            
        
        
        return self.board

    def printBoard(self,board):
        
        for col in range(len(board)):
            
            for row in range(len(board[col])):
                print(board[col][row])
                print(" ")
                
            print("\n")
                

    def possibleMoves(self):
        return []

    def legalMoves(self):
        return []

    def examineState(self):
        return []


def main():
    solve = boggleSolver()
    myboard = solve.loadBoard('boardex')
    solve.printBoard(myboard)
    

if __name__ == "__main__":
    main()
        
