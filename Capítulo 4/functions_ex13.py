#!/usr/bin/env python3

def get_index(vals, item, occurrence):
    start_at = 0
    for x in range(occurrence):
        found_at = vals.index(item, start_at)
        start_at = found_at + 1
    return found_at


values = [99, 100, 88, 3, 100, 100, 42, 100, 88, 99, 100]
find_me = 100

for offset in range(1, 8):
    print(f"Occurrence {offset} of {find_me} is at",
          get_index(values, find_me, offset))
