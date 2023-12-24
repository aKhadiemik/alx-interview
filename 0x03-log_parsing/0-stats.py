#!/usr/bin/python3
"""
Module reads script from stdin and computes metrics
"""

import sys

lineNumber = 0
status_codes = {}
possible_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
file_size = 0


def printstats():
    """
    Display computed statistics
    """
    print(f"File size: {file_size}")
    for status, count in sorted(status_codes.items()):
        print(f"{status}: {count}")


try:
    for line in sys.stdin:
        try:
            line = line.split()
            file_size = int(line[-1])
            code = int(line[-2])
            if code in possible_status_code and isinstance(code, int):
                file_size += file_size
                lineNumber += 1
                if code in status_codes:
                    status_codes[code] += 1
                else:
                    status_codes[code] = 1
            if (lineNumber % 10) == 0:
                printstats()
        except ValueError:
            pass
except KeyboardInterrupt:
    sys.exit(0)
finally:
    printstats()
