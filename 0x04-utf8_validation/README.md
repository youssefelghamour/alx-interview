# 0x04. UTF-8 Validation

## Overview

The 0x04. UTF-8 Validation project involves implementing a method to validate whether a given dataset represents a valid UTF-8 encoding.

### Process

To determine if a dataset is a valid UTF-8 encoding:

- **Single-byte Characters**: Validate directly against UTF-8 rules where the leading bit is `0`.
- **Multi-byte Characters**: Check and verify byte sequences based on UTF-8 leading byte patterns (`110`, `1110`, `11110`) and continuation bytes (`10`).

## Function Description

### `validUTF8(data)`

- **Input**: A list of integers, each representing 1 byte of data (8 least significant bits).
- **Output**: `True` if `data` is a valid UTF-8 encoding, `False` otherwise.
- **Returns**: Boolean indicating the validity of the UTF-8 encoding.

### Implementation Details

- **Binary Conversion**: Convert each integer in `data` to an 8-bit binary representation.

- **Validation Process**:
  1. **Single-byte Characters**: Check if the binary string starts with '0'.
  2. **Multi-byte Characters**: 
     - Two-byte: Verify the sequence starts with '110' followed by '10'.
     - Three-byte: Verify '1110' followed by two '10' sequences.
     - Four-byte: Verify '11110' followed by three '10' sequences.
  
- **Return Value**: Returns `True` if all binary representations in `data` conform to UTF-8 encoding rules; otherwise, returns `False`.

### Usage

Use the following script `0-main.py` to test the function:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
```
