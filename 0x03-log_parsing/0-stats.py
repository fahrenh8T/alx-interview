#!/usr/bin/python3
import sys
import signal

def signal_handler(signum, frame):
    """Handles the interrupt signal to print the message before exiting."""
    print_stats(total_file_size, status_codes)
    sys.exit(0)

def print_stats(total_file_size, status_codes):
    """Prints the statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

# Setup signal handler for catching CTRL+C
signal.signal(signal.SIGINT, signal_handler)


total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}
line_counter = 0

try:
    for line in sys.stdin:
        # Attempt to parse the input line by line according to the expected format
        try:
            parts = line.split()
            ip, _, _, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[-2], parts[-1]
            file_size = int(file_size)  # Convert file size to integer
            # Update total file size and status code counts
            total_file_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            continue

        line_counter += 1
        if line_counter % 10 == 0:
            print_stats(total_file_size, status_codes)

except KeyboardInterrupt:
    pass

finally:
    print_stats(total_file_size, status_codes)
