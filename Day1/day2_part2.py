# Read in input
# Split into two lists
# Sort each list
# Determine how many times each item in list A appears in list B
# Sum the differences
# Print the sum



# Count how many times a number appears in a provided list
def countItems(list, number):
    count = 0
    for item in list:
        if item == number:
            count += 1
    return count

# Read in input from text file
with open('Day1/input.txt') as f:
#with open('Day1/input_example.txt') as f:
    input = f.read().splitlines()

    listA = []
    listB = []

    # Split into two lists
    for line in input:
        listA.append(line.split()[0])
        listB.append(line.split()[1])

    # Calculate the number of times each item in list A appears in list B
    similarityScore = 0
    for index in range(len(listA)):
        score = int(listA[index]) * countItems(listB, listA[index])
        similarityScore += score


    # Print the result
    print(similarityScore)
