#!/usr/bin/python3
""" log parsing """
import sys
import re

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

# Regular expression to match the input format
log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) '  # IP address
    r'- \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '  # Date & Time
    r'"GET /projects/260 HTTP/1\.1" '  # Request line
    r'(\d{3}) '  # Status code
    r'(\d{1,4})$'  # File size
)


def print_logs(total_size, status_counts):
    """ prints logs """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        # Match the line with the regex pattern
        match = log_pattern.match(line)
        if match:
            ip_address = match.group(1)
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update total file size
            total_file_size += file_size

            # Update status code counts if it's in the predefined set
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count == 10:
                line_count = 0
                print_logs(total_file_size, status_code_counts)
except KeyboardInterrupt:
    # Print logs on keyboard interruption
    print_logs(total_file_size, status_code_counts)
