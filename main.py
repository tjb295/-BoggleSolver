#### Boggle Solver Main ####
#### By Thomas Back     ####
#### 1/24/2018 CS470    ####

import time

class boggleSolver:
    
    def __init__(self, dic):
        self.board = []
        self.n = 0
        self.completeWords = []
        self.dic = dic

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
            
 
                
    def withinBoundsCheck(self, Position):
        #Helper function that returns false if the positions are less than 0 or greater than or equal to the max, N
        
        if Position[0] < 0 or Position[0] >= self.n:
            return False
        
        if Position[1] < 0 or Position[1] >= self.n:
            return False

        return True

    def possibleMoves(self, currPos):
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

    def examineState(self, currPos, path, word):

        path.append(currPos)

        for i in path:
            word += self.board[i[0]][i[1]]
        #compute new paths to begin search with first gaining possible moves
        possible = self.possibleMoves(currPos)

        #now compute the legal moves in those direction
        legal = (possible, path)

        #now compute the word that should be formed 
        word = word.lower()

        if word in self.dic:
            
            #check to see if the word is complete and then return after appending
            if word + "\n" in self.dic:
                self.completeWords.append(word)
                return

            #recursive element to begin search in new path
            for next in legal:
                examineState(next, path, word)
        else:
            return 






def main():
    begin = time.time()
    
    #open dictionary for reading
    dic = open(dictionary)
    dic = dic.read()

    #load board and begin the solution
    solve = boggleSolver(dic)
    myboard = solve.loadBoard('fourboard3.txt')
    solve.printBoard(myboard)

    #begin with empty list 
    myboard.examineState([0,0], [], '\n')

    
if __name__ == "__main__":
    main()
        
