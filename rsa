#!/usr/bin/python3
import sys
import time

def factorize_rsa_challenge(n):
    p = 2
    while n % p != 0:
        p += 1
    q = n // p
    return (p, q)

def factorize_all_rsa_challenge(filename):
    with open(filename, 'r') as file:
        numbers = file.read().strip().split('\n')
    
    for num in numbers:
        num = int(num)
        primes = factorize_rsa_challenge(num)
        print(f"{num}={primes[0]}*{primes[1]}")

if __name__ == "__main__":
    start_time = time.time()
    filename = sys.argv[1]
    factorize_all_rsa_challenge(filename)
    end_time = time.time()
    print("\nExecution time:", round(end_time - start_time, 3), "seconds")
