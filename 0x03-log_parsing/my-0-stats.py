#!/usr/bin/python3
"""
module contains a script that reads stdin line by line and computes metrics
"""
import sys


def print_values(file_total_size, status_codes):
    print('File size: {}'.format(file_total_size))

    for status_code in sorted(status_codes):
        if status_codes[status_code] > 0:
            print('{}: {}'.format(status_code, status_codes[status_code]))


def main():
    file_total_size = 0
    status_codes = {}

    try:
        line_count = 0

        # Read input from stdin
        for line in sys.stdin:
            line_count += 1

            parts = line.strip().split()
            if (len(parts) != 9):
                return
            [ip_address, dash, date1,
             date2, request1, request2, request3,
             status_code, file_size] = parts[:9]

            if not status_code.isdigit():
                return
            status_code = int(status_code)
            file_size = int(file_size)
            file_total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_values(file_total_size, status_codes)

    except KeyboardInterrupt:
        print_values(file_total_size, status_codes)


if __name__ == "__main__":
    main()
