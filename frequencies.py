"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        strItem = str(item)
        if strItem in frequencies:
            frequencies[strItem] = frequencies[strItem] + 1
        else:
            frequencies[strItem] = 1
    return frequencies
