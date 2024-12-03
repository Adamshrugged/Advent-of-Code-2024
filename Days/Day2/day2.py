# Read in input
# Split into five lists
# The lists need to be compared to see if all the numbers are either increasing or decreasing
# The differences between each number must be at least 1 and up to three


def differences(list):
    newList = []
    testList = list[0]

    pos = [1, 2, 3]
    neg = [-1, -2, -3]

    safeCount = 0

    for item in list:
        if( sequentials(item, pos) or sequentials(item, neg) ):
            safeCount += 1

    print(safeCount)


# Checks what the differences is between each element in the list and returns true if it is within the allowable
def sequentials(list, allowable):
    for index in range(0, len(list)-1):
        diff = int(list[index]) - int(list[index + 1])
        if diff not in allowable:
            return False
    return True


# Read in input from text file
with open('Day2/input.txt') as f:
#with open('Day2/input_example.txt') as f:
    input = f.read().splitlines()

    listA = []

    # Split into individual elements
    for line in input:
        listA.append(line.split())

    # Check what difference in numbers are
    differences(listA)