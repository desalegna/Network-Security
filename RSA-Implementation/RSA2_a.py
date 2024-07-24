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

def find_prime_factor(n):
    """Find one prime factor of n."""
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return n

def decrypt_message(encrypted_message, public_key):
    """Decrypt a message using the RSA algorithm."""
    e, n = public_key
    
    # Calculate p and q
    p = find_prime_factor(n)
    q = n // p
    
    # Calculate phi(n)
    phi = (p - 1) * (q - 1)
    
    # Calculate the private exponent d
    d = mod_inverse(e, phi)

    
    # Decrypt each number in the message
    decrypted_message = [pow(c, d, n) for c in encrypted_message]
    
    return decrypted_message

# Given public key
e = 12413
n = 13289

# Given encrypted message
encrypted_message = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]

# Calculate p and q
p = find_prime_factor(n)
q = n // p

# Display the values of p and q
print("p:", p)
print("q:", q)

# Calculate phi(n)
phi = (p - 1) * (q - 1)

# Calculate the private key d
d = mod_inverse(e, phi)

# Display the public key and private key
print("Public key: (e={}, n={})".format(e, n))
print("Private key: (d={}, n={})".format(d, n))

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, (e, n))

print("Decrypted message:", decrypted_message)
