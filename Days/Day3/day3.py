# Read in input
# Combine all lines into one
# Look for pattern of mul(#,#)
# Anything that doesn't following this should break
# including spaces, etc.

# Regex
import re

# function which scans for string like "mul(#,#)"
def scanText(txt):
    # regex pattern
    pattern = re.compile("mul\(([0-9]+),([0-9]+)\)")
    
    # create list of matches
    matches = pattern.findall(txt)
    # return list of matches
    return matches
    
# function which multiples and sums all of the provided lists of number pairs
def multiplyAndSum(listOfPairs):
    # create list to hold the results
    results = 0
    # iterate over list of pairs
    for pair in listOfPairs:
        # multiply the pair
        result = int(pair[0]) * int(pair[1])
        # add to
        results += result
    
    # return the sum
    return results

def __main__():
    fullString = ""

    # Read in input from text file
    with open('Days/Day3/input.txt') as f:
    #with open('Day2/input_example.txt') as f:
        input = f.read().splitlines()
        #input = f.read()

        # Split into individual elements
        for line in input:
            fullString += line

    print( multiplyAndSum(scanText(fullString)) )


__main__()