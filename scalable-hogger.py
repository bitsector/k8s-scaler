#!/usr/bin/env python3

import numpy as np
import time
import threading
from flask import Flask, jsonify

app = Flask(__name__)

# Global variables
task_thread = None
stop_event = threading.Event()

def cpu_intensive_task(size):
    while not stop_event.is_set():
        a = np.random.rand(size, size)
        b = np.random.rand(size, size)
        result = np.dot(a, b)
        print(f"Matrix multiplication completed. Result shape: {result.shape}")
        time.sleep(0.1)

@app.route('/start/<int:size>')
def start_task(size):
    global task_thread, stop_event
    if task_thread and task_thread.is_alive():
        return jsonify({"message": "Task is already running"}), 400
    
    stop_event.clear()
    task_thread = threading.Thread(target=cpu_intensive_task, args=(size,))
    task_thread.start()
    return jsonify({"message": f"Started CPU-intensive task with matrix size {size}x{size}"}), 200

@app.route('/stop')
def stop_task():
    global task_thread, stop_event
    if not task_thread or not task_thread.is_alive():
        return jsonify({"message": "No task is currently running"}), 400
    
    stop_event.set()
    task_thread.join()
    return jsonify({"message": "CPU-intensive task stopped"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
