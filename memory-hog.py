#!/usr/bin/env python3

import time

# Allocate a large list (approximately 512 MB)
x = [0] * (1024 * 1024 * 1024)

# Sleep to keep the memory allocated
while True:
    time.sleep(1000000)
