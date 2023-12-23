import math
import multiprocessing


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def find_primes(start, end):
    primes = []
    for n in range(start, end):
        if is_prime(n):
            primes.append(n)
    return primes


def find_primes_multiprocessing(start, end, num_processes):
    pool = multiprocessing.Pool(processes=num_processes)
    chunk_size = (end - start) // num_processes
    ranges = [(start + i*chunk_size, start + (i+1)*chunk_size) for i in range(num_processes)]
    result = pool.starmap(find_primes, ranges)
    pool.close()
    pool.join()
    primes = sum(result, [])
    return primes


primes = find_primes_multiprocessing(0, 100000, 4)
print(primes)
