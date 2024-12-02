# Read in input
# Split into five lists
# The lists need to be compared to see if all the numbers are either increasing or decreasing
# The differences between each number must be at least 1 and up to three


def differences(list):

    pos = [1, 2, 3]
    neg = [-1, -2, -3]

    safeCount = 0

    for item in list:
        isSafe = False
        newList = []

        # Check each permutation of the list without a single element
        for index in range(0, len(item)):
            newList = partialLists(item, index)
            if( sequentials(newList, pos) or sequentials(newList, neg) ):
                safeCount += 1
                break

    print(safeCount)

# Returns a new list without the index of the list
def partialLists(list, index):
    newList = []
    for i in range(0, len(list)):
        if i != index:
            newList.append(list[i])
    return newList

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