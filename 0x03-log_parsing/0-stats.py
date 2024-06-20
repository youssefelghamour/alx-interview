#!/usr/bin/python3
""" log parsing """
import sys


def print_logs(status_counts, total_size):
    """ Print current statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_file_size += int(parsed_line[0])
                status_code = int(parsed_line[1])

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            if line_count == 10:
                line_count = 0
                print_logs(status_code_counts, total_file_size)
finally:
    print_logs(status_code_counts, total_file_size)
