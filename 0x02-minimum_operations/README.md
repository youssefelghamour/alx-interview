# 0x02. Minimum Operations

## Overview

The `0x02. Minimum Operations` project involves implementing a method to calculate the fewest number of operations needed to result in exactly `n` characters of `'H'` in a text file (that has a single character `H`). The text editor can only execute two operations: Copy All and Paste.

### Methodology

1. The file contains a single character 'H'.
2. Determine the optimal sequence of operations (Copy All and Paste) to reach exactly `n` characters.
3. The operations should be minimized, and the total number of operations is returned.

## Process

To determine the fewest number of operations:

- Factorize the number `n` into its prime factors.
- The sum of these prime factors represents the minimum number of operations needed.

## Example

For `n = 9`:

`H` => `Copy All` => `Paste` => HH => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

## Function Description

### `minOperations(n)`

- **Input**: An integer `n`.
- **Output**: An integer representing the minimum number of operations.
- **Returns**: The minimum number of operations required to get exactly `n` characters, or `0` if `n` is impossible to achieve.

### Implementation Details

The function follows these steps:
1. If `n` is less than or equal to 1, return 0 (impossible to achieve).
2. Factorize `n` into its prime factors.
3. Sum the prime factors to get the minimum number of operations.

### Usage

Use the following script `0-main.py` to test the function:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

Running the test:

```
$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```
