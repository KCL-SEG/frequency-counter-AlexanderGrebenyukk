"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        found = False
        if item in frequencies:
            frequencies[item] += 1
            break
        else:
            frequencies[item] = 1
    return frequencies
