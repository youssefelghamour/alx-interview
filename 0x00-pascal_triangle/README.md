# 0x00. Pascal's Triangle

This project involves creating a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s Triangle with `n` levels.

## Function Description

### `pascal_triangle(n)`
- **Input**: An integer `n`.
- **Output**: A list of lists of integers representing Pascal's Triangle with `n` levels.
- **Returns**: An empty list if `n <= 0`.

### Usage

Use the following script 0-main.py to test the function:
```
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

Running the test:
```
$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
