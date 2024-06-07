# 0x01. Lockboxes

## Overview

The `0x01. Lockboxes` project involves implementing a method to determine if all the boxes in a collection of locked boxes can be opened. The method `canUnlockAll(boxes)` takes a list of lists as input, where each inner list represents a box and contains the keys to other boxes.

1. The function begins with the first box always unlocked.
2. It iterates through each key found in the unlocked boxes.
3. Each key is attempted to be used to unlock the corresponding box.
4. If a box can be unlocked, the process is repeated for that box.
5. This iterative process continues until either no more boxes can be unlocked or until all boxes are unlocked.
6. If all boxes are successfully unlocked, the function returns `True`; otherwise, it returns `False`.

## Example

boxes = [[1, 2], [2, 3], [4], [0], []]

1. Start with the first box, `boxes[0]`, which is already unlocked.
   - `queue = [0]`
   - `unlocked_boxes = [0]`

2. Check the keys inside `boxes[0]`, which are 1 and 2.  
   - `queue = [1, 2]`
   - `unlocked_boxes = [0, 1, 2]`

3. Use key 1 to unlock `boxes[1]`.  
   - `queue = [2, 3]`
   - `unlocked_boxes = [0, 1, 2, 3]`

6. Now, go back to the keys in the queue. Use key 2 to unlock `boxes[2]`.  
   - `queue = [3, 4]`
   - `unlocked_boxes = [0, 1, 2, 3, 4]`

7. Use key 3 to unlock `boxes[3] = [0]`.
   - `queue = [4]`
   - `unlocked_boxes = [0, 1, 2, 3, 4]`

8. Use key 4 to unlock `boxes[4] = []`.  
   - `queue = []`
   - `unlocked_boxes = [0, 1, 2, 3, 4]`

9. queue is empty and All boxes are successfully unlocked.  

10. Return True.


## Function Description

### `canUnlockAll(boxes)`
- **Input**: A list of lists `boxes`.
- **Output**: Boolean value.
- **Returns**: `True` if all boxes can be opened; `False` otherwise.

### Usage
Use the following script main_0.py to test the function:
```
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

Running the test:
```
$ ./main_0.py
True
True
False
```
