"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        found = False
        for storedItem in frequencies:
            if(item!=storedItem):
                pass
            else:
                found = True
                frequencies[item] = frequencies.get(item) + 1
                break

        if(found == False):
            frequencies[item] = 0


    return frequencies
