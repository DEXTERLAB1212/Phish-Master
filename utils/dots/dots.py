import time

def print_dots(num_dots, delay=0.5):
    for _ in range(num_dots):
        print(".", end="", flush=True)  # Print dot without newline
        time.sleep(delay)  # Delay between dots
    print()
