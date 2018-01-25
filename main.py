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
        print(board)
        board.strip(' ')

        #for loop to loop through letters, disregards white space
        for letter in range(len(board)):
            #if reached new line, save that dimension within array
            if board[letter] == '\n':
                self.board.append(temp)
                temp = []
                count = 0
                
            #if blank space, skip
            elif board[letter] == " ":
                continue
            

            else :
                temp.append(board[letter])
                count += 1
            
        
        
        return self.board

    def printBoard(self,board):
        printLine = ""

        for col in range(len(board)):
            
            for row in range(len(board[col])):
                printLine = printLine + board[col][row] + " "
                
            print(printLine)
            printLine = ""
                

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
        
