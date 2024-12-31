import numpy as np
import argparse
import time

def cpu_intensive_task(size):
    a = np.random.rand(size, size)
    b = np.random.rand(size, size)
    return np.dot(a, b)

def main():
    parser = argparse.ArgumentParser(description="Resource hogger for testing autoscalers in Kubernetes")
    parser.add_argument("-s", "--size", type=int, required=True, help="Size of the matrix for multiplication")
    args = parser.parse_args()

    print(f"Starting CPU-intensive task with matrix size {args.size}x{args.size}")
    
    while True:
        start_time = time.time()
        result = cpu_intensive_task(args.size)
        end_time = time.time()
        
        print(f"Matrix multiplication completed in {end_time - start_time:.4f} seconds")
        print(f"Result shape: {result.shape}")
        print("----")
        
        # Small delay to prevent overwhelming the system
        time.sleep(0.1)

if __name__ == "__main__":
    main()
