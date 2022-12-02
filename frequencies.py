"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        found = False
        if item in frequencies:
            frequencies[item] = frequencies[item] + 1
            break
        else:
            try:
                frequencies[int(item)] = 1
            except:
                frequencies[item] = 1
    return frequencies
