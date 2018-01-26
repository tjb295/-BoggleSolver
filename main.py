#### Boggle Solver Main ####
#### By Thomas Back     ####
#### 1/24/2018 CS470    ####

import time

class boggleSolver:
    
    def __init__(self):
        self.board = []
        self.n = 0

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
                self.board.append(temp)
                temp = []
                if self.n == 0:
                    self.n = count
                count = 0
                
            #if blank space, skip
            elif board[letter] == " ":
                continue
            
            #append the letter to the temp array to be inserted as row into the board array
            else :
                temp.append(board[letter])
                count += 1
            
        
        
        return self.board

    def printBoard(self,board):

        #placeholder for a row of letters to be printed at once
        printLine = ""

        #with a 2d array we will have nested for loops to print from row and col
        for col in range(len(board)):
            
            for row in range(len(board[col])):
                printLine = printLine + board[col][row] + " "
                
            print(printLine)
            printLine = ""
            
        print(self.n)
                
    def withinBoundsCheck(self, Position):
        #Helper function that returns false if the positions are less than 0 or greater than or equal to the max, N
        
        if Position[0] < 0 or Position[0] >= self.n:
            return False
        
        if Position[1] < 0 or Position[1] >= self.n:
            return False

        return True

    def possibleMoves(self, currPos, board):
        #generates all possible next positions, (x-y pairs in a list, set or whatver you decide)
        #we could load currPos as a list of two elements, [0] always x, [1] always y
        #first check if the currpos is within the bounds of the board
        possMovesArr = []

        if not self.withinBoundsCheck(currPos):
            print("Error, current position is not within bounds\n")
            return -1
        
        #if within the bounds then move on
        currPos[0] += 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])

        currPos[1] += 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])

        currPos[0] -= 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])

        currPos[0] -= 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])
        
        currPos[1] -= 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])
        
        currPos[1] -= 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])
        
        currPos[0] += 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])
        
        currPos[0] += 1
        if self.withinBoundsCheck(currPos):
            possMovesArr.append(currPos[:])
        
        return possMovesArr


    def legalMoves(self, possibleMoves, visited):
        
        for i in possibleMoves:
            if i in visited:
                possibleMoves.remove(i)

        return possibleMoves

    def examineState(self):
        return []


def main():
    solve = boggleSolver()
    myboard = solve.loadBoard('boardex')
    solve.printBoard(myboard)
    possibles = solve.possibleMoves([2,2], myboard)
    print(possibles)
    print(solve.legalMoves(possibles, [[1,1], [3,1]]))
    

if __name__ == "__main__":
    main()
        
