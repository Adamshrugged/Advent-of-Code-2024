# Split file into two segments: page ordering rules & pages to produce in each update
# Page ordering rules:
#   If an update includes both numbers, then this is the order they should be printed
#   Though it does not need to be immediately preceeding


# Need to determine rules
# Check if both pages in the rule pairing are in the applicable update
# Make a list of the pages that are to be updated

import random

# See which rules pairings are in the lines
def check_rules(rules, updates):
    # See which rule pairings are in the lines
    applicable_rules = []
    for rule in rules:
        ruleaA = rule.split('|')[0]
        ruleaB = rule.split('|')[1]
        #print("Checking rule: " + ruleaA + " and " + ruleaB + " in ")
        #print(updates)
        if ruleaA in updates and ruleaB in updates:
            if rule not in applicable_rules:
                #print(" > Applicable rule: " + rule)
                applicable_rules.append(rule)
    
    return applicable_rules

# Read in file
def __main__():
    # Read in file
    with open("Days/Day5/input.txt") as f:
    #with open("Days/Day5/input_example.txt") as f:
        lines = f.readlines()
     # Remove newline characters
    lines = [line.strip() for line in lines]

    count_middles = 0

    # Split into the page ordering rules (contain '|' )
    rules = []
    for line in lines:
        if '|' in line:
            rules.append(line)
    
    # Split into the pages to be updated
    pages_updates = []
    for line in lines:
        if ',' in line:
            pages_updates.append(line)
    
    #print(pages_updates)

    # See which rule pairings are in the lines
    #print(rules)
    
    for updates in pages_updates:
        applicable_rules = check_rules(rules, updates)

        #print(applicable_rules)

        # Now ensure that the printed numbers are in the correct order
        new_order = updates.split(',')
        #print("Initial order: " + str(new_order))

        # Check the rules until no more swaps are needed
        fixed = False
        while not fixed:
            fixed = True
            for rule in applicable_rules:
                ruleaA = rule.split('|')[0]
                ruleaB = rule.split('|')[1]
                indexA = new_order.index(ruleaA)
                indexB = new_order.index(ruleaB)
                # Check position of ruleaA in new_order vs. ruleaB
                if new_order.index(ruleaA) > new_order.index(ruleaB):
                    # Swap positions of ruleaA and ruleaB in new_order
                    new_order[indexA], new_order[indexB] = new_order[indexB], new_order[indexA]
                    fixed = False

        # For only the updates that were NOT updated to a new order
        #print("Comparing updates and new updates: " + str(updates) + " and " + str(new_order))
        if( updates != ','.join(new_order)):
            # Get only the middle number based on index from each listw
            # find the halfway index of the list
            middle_index = int(len(new_order)/2)
            middle_number = new_order[middle_index]
            #print("Middle number: " + middle_number)
            count_middles += int(middle_number)
            #print("Middle number: " + middle_number)
    
    print("Count of middles: " + str(count_middles))

__main__()