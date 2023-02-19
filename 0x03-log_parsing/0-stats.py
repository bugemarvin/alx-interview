#!/usr/bin/python3
'''
log pahsing for display
'''
import sys

total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin):
        # Skip lines that don't match the expected format
        parts = line.split()
        if len(parts) != 7 or parts[2] != 'GET' or not parts[3].startswith('/projects/') or not parts[4].isdigit() or not parts[5].isdigit():
            continue

        # Extract status code and file size
        status_code = int(parts[4])
        file_size = int(parts[5])

        # Update total file size
        total_size += file_size

        # Update status code counts
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        # Print statistics after every 10 lines
        if (i + 1) % 10 == 0:
            print(f'Total file size: {total_size}')
            for status_code in sorted(status_counts.keys()):
                print(f'{status_code}: {status_counts[status_code]}')

except KeyboardInterrupt:
    # Handle keyboard interruption by printing final statistics
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts.keys()):
        print(f'{status_code}: {status_counts[status_code]}')
