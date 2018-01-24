#### Boggle Solver Main ####
#### By Thomas Back     ####
#### 1/24/2018 CS470    ####

import time

class boggleSolver:
    
    def __init__(self):
        self.board = []

    #loads NxN board into matrix
    def loadBoard(boardFile):
        #temp array
        temp = []
        count = 0
        
        board = open(boardFile)
        board.strip(" ")

        #for loop to loop through letters, disregards white space
        for letter in board:

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
                count ++
            
        
        
        return self.board

    def printBoard():

    def possibleMoves():

    def legalMoves():

    def examineState():


def main():
    solve = boggleSolver()
    myboard = solve.loadBoard("board.txt")
    solve.printBoard(myboard)
    

if __name__ == "__main__":
    main()
        
