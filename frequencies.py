"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        try:
            if int(item) in frequencies:
                frequencies[item] = frequencies[item] + 1
            else:
                frequencies[item] = 1
        except:
            if item in frequencies:
                frequencies[item] = frequencies[item] + 1
            else:
                frequencies[item] = 1
    return frequencies
