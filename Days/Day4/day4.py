# Read in input
# Need to map letters onto nodes and search for the number of times
# that the word 'XMAS' appears adjacent

# Regex
import re


# Return sequence of characters from the given location in the map
def getSequence(locX, locY, charMap):
    pattern = 'XMAS'

    # Only check if starts with X
    if(charMap[locY][locX] == 'X'):
        # HORIZONTAL
        if( locX + 3 < len(charMap[locY]) ):
            if( charMap[locY][locX + 1] == 'M' and \
            charMap[locY][locX + 2] == 'A' and \
            charMap[locY][locX + 3] == 'S' ):
                return True
        if( locX - 3 >= 0 ):
            if( charMap[locY][locX - 1] == 'M' and \
            charMap[locY][locX - 2] == 'A' and \
            charMap[locY][locX - 3] == 'S' ):
                return True
        # VERTICAL
        if( locY + 3 < len(charMap) ):
            if( charMap[locY + 1][locX] == 'M' and \
            charMap[locY + 2][locX] == 'A' and \
            charMap[locY + 3][locX] == 'S' ):
                return True
        if( locY - 3 >= 0 ):
            if( charMap[locY - 1][locX] == 'M' and \
            charMap[locY - 2][locX] == 'A' and \
            charMap[locY - 3][locX] == 'S' ):
                return True
        # DIAGONAL
        if( locY + 3 < len(charMap) and locX + 3 < len(charMap[locY]) ):
            if( charMap[locY + 1][locX + 1] == 'M' and \
            charMap[locY + 2][locX + 2] == 'A' and \
            charMap[locY + 3][locX + 3] == 'S' ):
                return True
        if( locY - 3 >= 0 and locX - 3 >= 0 ):
            if( charMap[locY - 1][locX - 1] == 'M' and \
            charMap[locY - 2][locX - 2] == 'A' and \
            charMap[locY - 3][locX - 3] == 'S' ):
                return True
        if( locY - 3 >= 0 and locX + 3 < len(charMap[locY]) ):
            if( charMap[locY - 1][locX + 1] == 'M' and \
            charMap[locY - 2][locX + 2] == 'A' and \
            charMap[locY - 3][locX + 3] == 'S' ):
                return True
        if( locY + 3 < len(charMap) and locX - 3 >= 0 ):
            if( charMap[locY + 1][locX - 1] == 'M' and \
            charMap[locY + 2][locX - 2] == 'A' and \
            charMap[locY + 3][locX - 3] == 'S' ):
                return True
        




        return False

        

    return False


def __main__():
    charMap = []
    xmasCount = 0
    # Read in input from text file
    with open('Days/Day4/input.txt') as f:
    #with open('Days/Day4/input_example.txt') as f:
        input = f.read().splitlines()
        #input = f.read()

        # make 2d array of characters from each line
        charMap = [list(line) for line in input]
    
    # Iterate through the map and find the number of times XMAS appears
    for y in range(len(charMap)):
        for x in range(len(charMap[y])):
            if(getSequence(x, y, charMap)):
                xmasCount += 1
    
    # Print the number of times XMAS was found
    print("Found XMAS " + str(xmasCount) + " times")


__main__()