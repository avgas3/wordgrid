import re

# the size of the grid we are searching for
target = 6

# read the wordlist, using only the first token of each line, converted to lowercase
with open("common") as f:
    wordlist = [x.split()[0].lower() for x in f.readlines()]
# select the words of the target length    
words = [x for x in wordlist if len(x) == target] 

# initialize our grid with . characters
grid = ["."*target] * target

# keep track of the search index for each level
indexes = [0]*target
level = 0

def wordmatch(pattern):
    return bool([x for x in words if re.search(pattern, x) and x not in grid]) # ensures no duplicate words

# will end when level reaches -1, meaning the program has finished searching all grids.
while level >= 0:
    
    # load the next word in the list for the current level
    try:
        w = words[indexes[level]]
        indexes[level] += 1

    # if the end of the list has been reached, go down back a level.
    except IndexError:
        w = -1
        indexes[level] = 0        
        grid[level] = "."*target
        level = level - 1
    
    # update the grid with the new word
    else:
        grid[level] = w
        match = True
        
        # treat each column like a regex pattern, and check that at least 1 match exists
        for i in range(target):
            pattern = "".join([x[i] for x in grid])
            if not wordmatch(pattern):
                match = False        
                break
        
        # if a word exists for each column, go to the next level
        if match:
            level = level + 1
            # if we just placed the final word, print the grid and continue searching for more. 
            if level == target:
                print(grid)
                level = level - 1

