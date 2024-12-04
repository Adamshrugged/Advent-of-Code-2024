# Read in input
# Need to map letters onto nodes and search for the number of times
# that the word 'XMAS' appears adjacent

# Regex
import re


# Return sequence of characters from the given location in the map
def getSequence(charMap):
    totals = 0
    numrows = len(charMap)
    numcols = len(charMap[0])

    for r in range(1, numrows-1):
        for c in range(1, numcols-1):
            first = charMap[r-1][c-1] + charMap[r][c] + charMap[r+1][c+1]
            second = charMap[r-1][c+1] + charMap[r][c] + charMap[r+1][c-1]
            if first in ('MAS', 'SAM') and second in ('MAS', 'SAM'):
                totals += 1
    
    return totals


def __main__():
    charMap = []
    # Read in input from text file
    #with open('Days/Day4/input.txt') as f:
    with open('Days/Day4/input.txt') as f:
        input = f.read().splitlines()
        #input = f.read()

        # make 2d array of characters from each line
        charMap = [list(line) for line in input]
    
    # Iterate through the map and find the number of times XMAS appears
    xmasCount = getSequence( charMap )
    
    # Print the number of times XMAS was found
    print("Found X-MAS " + str(xmasCount) + " times")


__main__()