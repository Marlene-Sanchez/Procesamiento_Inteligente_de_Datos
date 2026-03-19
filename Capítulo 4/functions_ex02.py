#!/usr/bin/env python3

def get_max_length(data):
    return len(max(data, key=len))


words = ["hello", "supercalafragalistic", "Q", "moose", "functions!"]
longest = get_max_length(words)

for word in words:
    print(f"{word:>{longest}s}")
