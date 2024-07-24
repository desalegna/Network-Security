import time
import random
import math

# Pollard's rho algorithm for factorization
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    g = 1
    while g==1:             
        x = ((x * x) % n + c) % n
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n
        g = math.gcd(abs(x-y), n)
    return g

# Measure time taken for factorization as a function of bit size
def measure_time(bits):
    times = []
    for b in bits:
        n = random.getrandbits(b)
        start = time.time()
        _ = pollards_rho(n)
        end = time.time()
        times.append(end - start)
    return times

# Define a function to calculate complexities
def complexities(bits):
    complexities = []
    for b in bits:
        complexities.append(2 ** (b / 4))
    return complexities

# Bit sizes to test
bits = [512, 1024, 2048]

# Measure time taken for each bit size
times = measure_time(bits)

# Print the complexities and measured times
print("Bit Size | Complexity (O(N^(1/4))) | Time Taken")
for b, t, c in zip(bits, times, complexities(bits)):
    print(f"{b}-bit| O(2^{b/4}) = O({c})    | {t:.6f} seconds")
