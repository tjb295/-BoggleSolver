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
        self.moves = 0
        self.cleverness = False

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
                    self.n = count -1
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
        
        if Position[0] < 0 or Position[0] > self.n:
            return False
        
        if Position[1] < 0 or Position[1] > self.n:
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


    def legalMoves(self, possibleMoves, visited, word):
        valid = []
        for i in possibleMoves:
            if i not in visited:
                valid.append(i)

        return valid

    def examineState(self, currPosition, path, word):

        #hold the number of moves
        self.moves += 1
        path.append(currPosition[:])
        
        #build the word with the new letter in the current position
        word += self.board[currPosition[0]][currPosition[1]]
        

        #compute new paths to begin search with first gaining possible moves
        possible = self.possibleMoves(currPosition[:])

    
        #now compute the legal moves in those direction
        legal = self.legalMoves(possible, path, word)

        #now compute the word that should be formed 
        word = word.lower()


        if "\n" + word in self.dic:
            #check to see if the word is complete and then return after appending
            if ("\n" + word + "\n") in self.dic:
                if word not in self.completeWords:
                    self.completeWords.append(word[:])
        
            #recursive element to begin search in new path
            for next in legal:
                self.examineState(next[:], path[:], word)
        else:
            return 
    

def main():
    begin = time.time()
    
    #open dictionary for reading
    dic = open("twl06.txt")
    dic = dic.read()

    #load board and begin the solution
    solve = boggleSolver(dic)
    myboard = solve.loadBoard('fourboard2.txt')
    solve.printBoard(myboard)
    print("\n")

    solve.cleverness = True
    #begin with empty list 
    print("And we're off!")
    for k in range(solve.n + 1):
        for j in range(solve.n + 1):
            solve.examineState([k,j], [], "")

    end = time.time()
    print("All Done!")
    print("\n")

    #save the total time
    timeResult = end - begin
    print("Searched total of %d moves in %f seconds" % (solve.moves, timeResult))
    solve.completeWords.sort(key=len)
    print("Words found: ")

    #print array to loop through and hold words of same length
    printArr = []
    for words in range(len(solve.completeWords)):
        printArr.append(solve.completeWords[words])
        try:

            # if the length differs between indices, print and switch to next round of words
            if len(printArr[-1]) != len(solve.completeWords[words+1]):
                printArr.sort()
                print("%d %d-letter words: " % (len(printArr), len(printArr[-1])), end = "")
                for i in printArr:
                    print("%s, " % (i), end =""),
                print("\n")
                printArr = []

        except IndexError:
            printArr.sort()
            print("%d %d-letter words: " % (len(printArr), len(printArr[-1])), end = "")
            for i in printArr:
                print("%s, " % (i), end =""),
                printArr = []

    print("\n")

    print("Found %d words!" % (len(solve.completeWords)))
    print(solve.completeWords)

    
if __name__ == "__main__":
    main()
        
