# Read in input
# Combine all lines into one
# Look for pattern of mul(#,#)
# Anything that doesn't following this should break
# including spaces, etc.

# Regex
import re
from operator import mul

# function which removes all strings that start with "don't" and end in "do"
def removeStrings(txt):
    # regex pattern
    pattern = r"don't\(\).*?do\(\)"
    
    return re.sub(pattern, '', txt)

# function which scans for string like "mul(#,#)"
def scanText(txt):
    # regex pattern
    pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    
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
    with open('Days/Day3/input2.txt') as f:
    #with open('Days/Day3/input_example.txt') as f:
        input = f.read().splitlines()

        # Split into individual elements
        for line in input:
            fullString += line

    # First remove all strings that start with "don't()" and end in "do()"
    fullString = removeStrings(fullString)
    # Now print everything else
    print( multiplyAndSum(scanText(fullString)) )


__main__()