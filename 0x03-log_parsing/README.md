# 0x03. Log Parsing

## Overview

The `0x03. Log Parsing` project involves real-time parsing and processing of log data from standard input (stdin). It focuses on extracting HTTP status codes from log entries and computing metrics such as total file size and status code counts, which are printed periodically or upon interruption.

### Methodology

1. Read log entries from stdin line by line.
2. Parse each line to extract relevant data points: IP address, date, HTTP method, status code, and file size.
3. Calculate the total file size accumulated from all entries.
4. Count occurrences of each HTTP status code (200, 301, 400, 401, 403, 404, 405, 500).
5. Print metrics after every 10 lines or upon keyboard interruption (CTRL + C).

## Example

For example, executing `0-generator.py | 0-stats.py` produces:

```
$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
$ 
```

## Function Description

### `0-stats.py`

The `0-stats.py` script reads log entries from stdin, processes each entry to extract IP address, date, HTTP method, status code, and file size, and computes the following metrics:

- **Total file size**: Accumulates the total file size from all log entries.
- **Number of lines by HTTP status code**: Counts occurrences of HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500) and prints them in ascending order.

Upon reading every 10 lines or upon interruption (CTRL + C), the script prints these metrics.

### Input Format

Each log entry is expected to be in the following format:

`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

For example:

`192.168.0.1 - [2024-06-27T10:15:30] "GET /projects/260 HTTP/1.1" 200 512`

### Implementation Details

The script:
1. Reads log entries from stdin and splits each line into components.
2. Reverses the order of components to extract file size and status code (elements 0 and 1).
3. Accumulates the total file size and updates counts for each HTTP status code.
4. Prints accumulated metrics every 10 lines or upon interruption.

### Usage

Execute the following commands to run the script:

```bash
./0-generator.py | ./0-stats.py
```
