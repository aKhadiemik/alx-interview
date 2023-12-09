#!/usr/bin/python3
"""
Boxes numbered 0 to n-1. Each box may contain keys to
the other boxes. Function determines whether all boxes
can be opened starting from box 0
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be unlocked otherwise False
    """
    n = len(boxes)
    visited = set([])
    unlocked = set([0])
    while len(unlocked) > 0:
        currentKey = unlocked.pop()
        locks = boxes[currentKey]
        visited.add(currentKey)
        if len(locks) > 0:
            for newKey in locks:
                if not (newKey in visited):
                    if newKey < len(boxes):
                        unlocked.add(newKey)
    if len(visited) == n:
        return True
    else:
        return False
