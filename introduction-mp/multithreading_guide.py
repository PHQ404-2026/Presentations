"""
multithreading_guide.py
A guide on multithreading in Python.
"""

import threading
import time


# -----------------------------
# 1. Basic functions
# -----------------------------
def print_numbers():
    """Print numbers 0-4 with a small delay, showing thread name."""
    for i in range(5):
        print(f"{threading.current_thread().name} prints {i}")
        time.sleep(0.5)


def greet(name, delay):
    """Print a greeting multiple times with a delay."""
    for _ in range(3):
        print(f"{threading.current_thread().name} says hello to {name}")
        time.sleep(delay)


counter = 0
counter_lock = threading.Lock()


def increment_counter():
    """Increment a shared counter safely using a lock."""
    global counter
    for _ in range(1000):
        with counter_lock:
            counter += 1


# -----------------------------
# 2. Main Program
# -----------------------------
if __name__ == "__main__":
    # --- Basic Threads ---
    print("\n--- Basic Threads ---")
    t1 = threading.Thread(target=print_numbers, name="Thread-1")
    t2 = threading.Thread(target=print_numbers, name="Thread-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Basic threads finished.\n")

    # --- Threads with Arguments ---
    print("--- Threads with Arguments ---")
    t3 = threading.Thread(target=greet, args=("Alice", 1), name="Greeter-1")
    t4 = threading.Thread(target=greet, args=("Bob", 0.7), name="Greeter-2")
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print("Greeting threads finished.\n")

    # --- Threads with Shared Counter and Lock ---
    print("--- Threads with Shared Counter ---")
    threads = [threading.Thread(target=increment_counter) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Counter value (should be 5000): {counter}\n")

# -----------------------------
# 3. Notes and Best Practices
# -----------------------------
"""
- Python threads are subject to the Global Interpreter Lock (GIL):
    * CPU-bound tasks may not see much speedup.
    * I/O-bound tasks (networking, file I/O) benefit most from threading.
- Use threading.Lock() to prevent race conditions when accessing shared data.
- Use thread.join() to wait for threads to finish before continuing.
- For CPU-bound tasks, consider using multiprocessing instead of threading.
"""
