"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if str(item) in frequencies:
            frequencies[item] = frequencies[item] + 1
        else:
            frequencies[str(item)] = 1
    return frequencies
