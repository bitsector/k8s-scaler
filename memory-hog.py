#!/usr/bin/env python3

import time
import signal
import sys
import argparse

def signal_handler(sig, frame):
    print("Memory hog stopped")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser(description='Memory hogger')
parser.add_argument('-m', '--memory', type=int, default=64,
                    help='Memory to allocate in MB (default: 64)')

args = parser.parse_args()

# Allocate a large list (size specified by command-line argument)
x = [0] * (args.memory * 1024 * 1024 // 8)  # Divide by 8 because each integer is 8 bytes

# Calculate actual memory usage
actual_memory = sys.getsizeof(x) + (len(x) * sys.getsizeof(0))

print(f"Requested memory: {args.memory} MB")
print(f"Actual memory allocated: {actual_memory / (1024 * 1024):.2f} MB")

# Sleep to keep the memory allocated
while True:
    time.sleep(1)
