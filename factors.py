#!/usr/bin/python3
import sys

def smallest_divisor(n):
    n = abs(n)
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def factors(x):
    q = smallest_divisor(x)
    p = x // q
    print(f"{x}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factors.py <file>")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                x = int(line.strip())
                factors(x)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
