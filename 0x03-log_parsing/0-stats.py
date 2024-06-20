#!/usr/bin/python3
""" log parsing """
import sys
import signal
import re

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Regex pattern to match the log format
log_format = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) '  # IP address
    r'- \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '  # Date & Time
    r'"GET /projects/260 HTTP/1\.1" '  # Request line
    r'(\d{3}) '  # Status code
    r'(\d{1,4})$'  # File size
)

total_size = 0
codes_to_print = {code: 0 for code in status_codes}
lines_processed = 0


def print_logs():
    """ Print current logs """
    print(f"File size: {total_size}")

    # print status codes in ascending order
    for code in sorted(codes_to_print.keys()):
        if codes_to_print[code] > 0:
            print(f"{code}: {codes_to_print[code]}")


def signal_handler(sig, frame):
    """ Handle SIGINT (Ctrl+C) by printing current statistics and exiting """
    print_logs()


# Register SIGINT signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Match the line with the regex pattern
        match = re.match(log_format, line.strip())
        if match:
            ip_address = match.group(1)
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update total file size
            total_size += file_size

            # Update status code count if it's in the predefined set
            if status_code in codes_to_print:
                codes_to_print[status_code] += 1

            lines_processed += 1

            # Print statistics every 10 lines
            if lines_processed == 10:
                print_logs()
                total_size = 0
                codes_to_print = {code: 0 for code in status_codes}
                lines_processed = 0

    # Print final statistics when stdin ends
    if lines_processed > 0:
        print_logs()

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print_logs()
    sys.exit(0)
