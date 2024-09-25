"""Converts an edge list into an adjacency list"""
X = [[1,3],[2,4],[3,5],[-1,1],[0,2],[-2,0]] # Original Data (Edge List)

keys = [] # Creates a list to store the keys which are every unique number in the dataset
values = [] # Creates a list to store the values for each key based on the original data

# This block of code uses X to makes the lists keys and values as follows
# keys:   [1, 3, 2, 4, 3, 5, -1, 1, 0, 2, -2, 0]
# values: [3, 1, 4, 2, 5, 3, 1, -1, 2, 0, 0, -2]
# The keys are all of the item from X in order and the values is the same thing 
# except the numbers from each list in X are reversed.
for i in range(len(X)): 
    keys.append(X[i][0]) # Adds the x coordinates to the keys list from before
    values.append(X[i][1])
    keys.append(X[i][1]) # Adds the y coordinates to the keys list from before
    values.append(X[i][0])

# This block of code take the values from the list keys to create a dictonary 
# with the list being the keys and the values being empty lists
# ans: {1: [], 3: [], 2: [], 4: [], 5: [], -1: [], 0: [], -2: []}
ans = {}
for i in range(len(keys)):
    ans[keys[i]] = []

# This block of code uses the values list and adds to the dictionary ans by
# adding the values to each key depending on the interactions listed in X
# ans: {1: [3, -1], 3: [1, 5], 2: [4, 0], 4: [2], 5: [3], -1: [1], 0: [2, -2], -2: [0]}
for i in range(len(values)):
    ans[keys[i]].append(values[i])
print(ans)
