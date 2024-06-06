#!/usr/bin/python3
"""  module for the Lockboxes function """


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened using keys found within the boxes

    Args:
    boxes (list of list of int): each list contains keys to other boxes

    Returns: true if all boxes can be opened, false otherwise
    """
    unlocked = [0]
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
                queue.append(key)

    return len(unlocked) == len(boxes)
