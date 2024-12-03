# Read in input
# Split into two lists
# Sort each list
# Calculate the difference between each element of the list, absolute value
# Sum the differences
# Print the sum


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

    # Sort each list
    listA.sort()
    listB.sort()

    # Calculate the difference between each element of the list, absolute value
    differences = 0
    for index in range(len(listA)):
        diff = abs(int(listA[index]) - int(listB[index]))
        differences += diff


    # Print the sum
    print(differences)