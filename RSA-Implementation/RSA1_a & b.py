import random

# Part a: Generating RSA key pair based on key size in bits

def is_prime(n, k=5):
    """Check if a number is prime using the Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    # Write n as 2^r*d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Miller-Rabin primality test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """Generate a prime number with the specified number of bits."""
    while True:
        p = random.randint(2**(bits-1), 2**bits - 1)
        if is_prime(p):
            return p

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular inverse of 'a' modulo 'm'."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits):
    """Generate an RSA key pair."""
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# Part b: RSA Encryption and Decryption

def encrypt(number, public_key):
    """Encrypt a number using the RSA algorithm."""
    e, n = public_key
    encrypted_number = pow(number, e, n)
    return encrypted_number

def decrypt(encrypted_number, private_key):
    """Decrypt an encrypted number using the RSA algorithm."""
    d, n = private_key
    decrypted_number = pow(encrypted_number, d, n)
    return decrypted_number

def main():
    # Generate an RSA key pair
    key_size_bits = 256
    public_key, private_key = generate_keypair(key_size_bits)
    print("Public key:", public_key)
    print("Private key:", private_key)

    # Number to encrypt
    number_to_encrypt = int(input("Enter a number to encrypt: "))

    # Encrypt the number
    encrypted_number = encrypt(number_to_encrypt, public_key)
    print("Encrypted number:", encrypted_number)

    # Decrypt the encrypted number
    decrypted_number = decrypt(encrypted_number, private_key)
    print("Decrypted number:", decrypted_number)

if __name__ == "__main__":
    main()
