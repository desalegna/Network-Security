import random

# Define the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_?.€0123456789"

# Function to find greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate random prime numbers
def random_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to check if a number is prime
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Function to generate RSA key pair
def generate_keypair(bits):
    p = random_prime(bits)
    q = random_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Function to transform text into numbers using the given coding scheme
def text_to_numbers(text):
    return [alphabet.index(char) for char in text]

# Function to transform numbers into text using the given coding scheme
def numbers_to_text(numbers):
    return ''.join([alphabet[num % len(alphabet)] for num in numbers])

# Function to encrypt a list of numbers (plaintext) using the public key
def encrypt(numbers, public_key):
    e, n = public_key
    encrypted_blocks = []
    block_size = len(str(n)) - 1  # Calculate block size based on n
    for i in range(0, len(numbers), block_size):
        block = numbers[i:i+block_size]
        num = 0
        for digit in block:
            num = num * len(alphabet) + digit
        encrypted_blocks.append(pow(num, e, n))
    return encrypted_blocks

# Function to decrypt a list of encrypted blocks using the private key
def decrypt(encrypted_blocks, private_key):
    d, n = private_key
    decrypted_numbers = []
    for block in encrypted_blocks:
        decrypted_block = pow(block, d, n)
        while decrypted_block > 0:
            decrypted_block, rem = divmod(decrypted_block, len(alphabet))
            decrypted_numbers.insert(0, rem)
    return decrypted_numbers

# Function to transform encrypted blocks into text
def encrypted_blocks_to_text(encrypted_blocks):
    encrypted_text = ""
    for block in encrypted_blocks:
        block_text = ""
        while block > 0:
            block, rem = divmod(block, len(alphabet))
            block_text = alphabet[rem] + block_text
        encrypted_text += block_text
    return encrypted_text

# Function to convert bytes to binary string
def bytes_to_binary(byte_string):
    return ''.join(format(byte, '08b') for byte in byte_string)

# Generate RSA key pair with 128 bits
public_key, private_key = generate_keypair(128)

# Display public and private keys
print("Public Key:", public_key)
print("Private Key:", private_key)

# Get message from the user
message = input("Enter your message: ")

# Transform message into numbers using the given coding scheme
numbers = text_to_numbers(message)
print("Message as numbers:", numbers)

# Encrypt the message
encrypted_blocks = encrypt(numbers, public_key)
print("Encrypted blocks:", encrypted_blocks)

# Transform encrypted blocks into alphabet text
encrypted_text = encrypted_blocks_to_text(encrypted_blocks)
print("Encrypted message:", encrypted_text)

# Decrypt the encrypted message
decrypted_numbers = decrypt(encrypted_blocks, private_key)
print("Decrypted numbers:", decrypted_numbers)

# Transform decrypted numbers into text
decrypted_text = numbers_to_text(decrypted_numbers)
print("Decrypted message:", decrypted_text)

# Convert encrypted message to binary
encrypted_binary = bytes_to_binary(encrypted_text.encode())

# Convert decrypted message to binary
decrypted_binary = bytes_to_binary(decrypted_text.encode())

# Print encrypted and decrypted messages in binary
print("Encrypted message (binary):", encrypted_binary)
print("Decrypted message (binary):", decrypted_binary)