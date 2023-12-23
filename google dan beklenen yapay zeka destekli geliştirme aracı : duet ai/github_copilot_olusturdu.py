import multiprocessing

def is_prime(n):

  if n <= 1:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True

def find_primes(start, end):

  primes = []
  for n in range(start, end):
    if is_prime(n):
      primes.append(n)

  return primes

if __name__ == "__main__":

  num_processors = multiprocessing.cpu_count()

  pool = multiprocessing.Pool(num_processors)

  chunks = [range(i, i + 100000) for i in range(0, end, 100000)]

  tasks = []
  for chunk in chunks:
    tasks.append((chunk[0], chunk[-1]))

  results = pool.map(find_primes, tasks)

  primes = []
  for result in results:
    primes += result

  print(primes)
