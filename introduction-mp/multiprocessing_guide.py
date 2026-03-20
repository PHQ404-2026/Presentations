"""
multiprocessing_guide.py
A guide on multiprocessing in Python.
"""

import multiprocessing
import time


# -----------------------------
# 1. Basic Functions
# -----------------------------
def print_numbers():
    """Print numbers 0-4 with a small delay, showing process name."""
    for i in range(5):
        print(f"{multiprocessing.current_process().name} prints {i}")
        time.sleep(0.5)


def greet(name, delay):
    """Print greeting multiple times with a delay."""
    for _ in range(3):
        print(f"{multiprocessing.current_process().name} says hello to {name}")
        time.sleep(delay)


def increment_counter(shared_counter, lock):
    """Increment a shared counter safely using a lock to prevent race conditions."""
    for _ in range(1000):
        with lock:  # Only one process can modify shared_counter at a time
            shared_counter.value += 1


def square(n):
    """Return the square of n, simulating a small workload."""
    time.sleep(0.2)  # Simulate CPU-bound work
    return n * n


def power_and_multiply(base, exponent, multiplier):
    """Return (base ** exponent) * multiplier."""
    time.sleep(0.1)  # Simulate CPU-bound work
    return (base**exponent) * multiplier


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


# -----------------------------
# 2. Main Program
# -----------------------------
if __name__ == "__main__":
    # --- Basic Processes ---
    print("\n--- Basic Processes ---")
    # Create two independent processes
    p1 = multiprocessing.Process(target=print_numbers, name="Process-1")
    p2 = multiprocessing.Process(target=print_numbers, name="Process-2")
    # Start the processes
    p1.start()
    p2.start()
    # Wait for both to finish
    p1.join()
    p2.join()
    print("Basic processes finished.\n")

    # --- Processes with Arguments ---
    print("--- Processes with Arguments ---")
    # Pass arguments to the target function using args
    p3 = multiprocessing.Process(target=greet, args=("Alice", 1), name="Greeter-1")
    p4 = multiprocessing.Process(target=greet, args=("Bob", 0.7), name="Greeter-2")
    p3.start()
    p4.start()
    p3.join()
    p4.join()
    print("Greeting processes finished.\n")

    # --- Shared Value with Lock ---
    print("--- Shared Counter with Lock ---")
    # multiprocessing.Value allows sharing simple data (like integers) across processes
    counter = multiprocessing.Value("i", 0)
    # Lock ensures only one process modifies the shared counter at a time
    lock = multiprocessing.Lock()
    # Create multiple processes that increment the shared counter
    processes = [
        multiprocessing.Process(target=increment_counter, args=(counter, lock))
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(f"Counter value (should be 5000): {counter.value}\n")

    # --- Using a Pool for Parallel Tasks ---
    print("--- Process Pool Examples ---")
    # A Pool manages multiple worker processes for parallel execution
    with multiprocessing.Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5]

        # 1. map(func, iterable)
        # Applies func to every item in iterable. Blocks until all results are ready.
        squares = pool.map(square, numbers)
        print(f"Squares with map: {squares}")

        # 2. starmap(func, iterable_of_tuples)
        # Like map(), but unpacks each tuple in the iterable as multiple arguments to func
        args_list = [(2, 3, 5), (3, 2, 4), (4, 2, 3)]
        results = pool.starmap(power_and_multiply, args_list)
        print(f"Starmap results (base**exp * mult): {results}")

        # 3. imap(func, iterable)
        # Returns an iterator and yields results as they are ready; allows incremental processing
        print("Results from imap:")
        for result in pool.imap(square, numbers):
            print(result)

        # 4. apply_async(func, args, callback)
        # Executes func asynchronously in a worker process.
        # Returns an AsyncResult object. Optionally, callback is called with the result.
        def print_result(res):
            print(f"Async result: {res}")

        async_results = [
            pool.apply_async(multiply, args=(i, i + 1), callback=print_result)
            for i in range(5)
        ]
        # Wait for all async results to complete
        for r in async_results:
            r.wait()

# -----------------------------
# 3. Notes and Best Practices
# -----------------------------
"""
- Multiprocessing bypasses Python's GIL, making it ideal for CPU-bound tasks.
- Use multiprocessing.Value or Array for shared memory; use Lock to avoid race conditions.
- Pool simplifies running many tasks in parallel:
    * map(func, iterable)       -> blocks until all results are ready
    * imap(func, iterable)      -> returns iterator; process results incrementally
    * starmap(func, iterable)   -> like map(), unpacks tuple arguments
    * apply_async(func, args)   -> asynchronous execution; optional callback
- Unless you know what you are doing, map and starmap are recommended.
- Always protect the entry point with `if __name__ == "__main__":` to avoid infinite process spawning.
"""
