
# Network Security- RSA Implementation


     Desalegn Aweke Wako

  

### Contents

- [RSA Implementation](#rsa-implementation)

- [1. RSA key pair generation & (de)encryption](#1-rsa-key-pair-generation-and-deencryption)
- [2. Test with a small key](#2-test-with-a-small-key)
  - [A. Decryption with small public exponent](#a-decryption-with-small-public-exponent)
  - [B. Complexity of factorization](#b-measeure-the-complexity-of-factorization)
  - [C. Decryption with large public exponent](#c-decryption-with-large-public-exponent)
- [3. RSA and Coding](#3-rsa-and-coding)



## Requirements
 - we have used Python programing language for implementating RSA

 ## RSA Implementation

This Python program demonstrates RSA encryption and decryption. RSA is a public-key cryptosystem widely used for secure communication. The implementation contain three major sections (R).
   - RSA key pair generation and (de)encryption
   - Test with a small key
   - RSA and Coding

 
## 1. RSA Key Pair generation and (de)encryption

    - Open the script `RSA1_a&b.py`
This program consists of two  parts:

1. **RSA key pair generation:** 
   - Generates an RSA key pair based on a specified key size in bits.
   - Uses the Miller-Rabin primality test to generate large prime numbers efficiently.
   - Implements functions to generate prime numbers, calculate modular inverse, and compute greatest common divisor.

2. **RSA Encryption and Decryption:**
   - Encrypts a user-input number using the RSA algorithm.
   - Decrypts the encrypted number using the RSA algorithm.

 **Understanding the Output:** Run the script `RSA1_a&b.py`
   - The program will display the generated public and private keys.
   - It will prompt you to enter a number to encrypt.
   - After encryption, it will display the encrypted number.
   - Finally, it will decrypt the encrypted number and display the decrypted result.

 [Sample Output]
  ```python
 Public key: (77810340953203243893824758633344660170375155427344979494480258225757004193287, 82382631190041907760777675041637581940328450745133202270974130105564442753243)
Private key: (80834140855902687531942878078045189276809641075211943643821665291106777407703, 82382631190041907760777675041637581940328450745133202270974130105564442753243)
Enter a number to encrypt: 639302
Encrypted number: 66162605237655315894087361479221389312912314973046750517434061353072097231619
Decrypted number: 639302
 ```

## 2. Test with a small key

In this section, we have three different expermentation

 ### A. Decryption with small public exponent

- Open the script `RSA2_a.py`

The program has the following features
  - it calculates the greatest common divisor of two numbers
  - it calculates the modular inverse of 'a' modulo 'm'
  - Finds prime factor of a given number
  - calculates the corresponding private key to decrypt the message.
  - Then decrypt the encrypted message


 **Understanding the Output:** Run the script `RSA2_a.py`
   - The program will display the generated prime numbers and private key.
   - finaly it will display the decrypted message.


[Sample Output]

```python
p: 97
q: 137
Public key: (e=12413, n=13289)
Private key: (d=3797, n=13289)
Decrypted message: [5424, 6221, 2423, 1662, 1023, 1362, 2917, 1023, 2028, 6215, 2427, 6210, 2121, 6229, 1714, 6215, 1828, 1762]
```


### B. Measeure the complexity of factorization

- Open the script `RSA2_b.py`

The program has the following features
  - The program utilizes pollard's rho algorithm to find a factorization of the number n by generating a pseudo-random sequence
  - Measure time taken for factorization as a function of bit size
  - Calculating complexities
  - Bit size to test


 **Understanding the Output:** Run the script `RSA2_b.py`
   - The program will display  complexities and time taken for factorization in terms of the size of a bits

[Sample Output]

```python
Bit Size | Complexity  (O(N^(1/4)))                 | Time Taken
512-bit  | O(2^128.0) = O(3.402823669209385e+38)    | 0.000000 seconds
1024-bit | O(2^256.0) = O(1.157920892373162e+77)    | 0.000000 seconds
2048-bit | O(2^512.0) = O(1.3407807929942597e+154)  | 0.000000 seconds
```

### C. Decryption with large public exponent

- Open the script `RSA2_c.py`

The program has the following features
  - it calculates the greatest common divisor of two numbers
  - it calculates the modular inverse of 'a' modulo 'm'
  - Finds prime factor of a given number
  - calculates the corresponding private key to decrypt the message.
  - Then decrypt the encrypted message


 **Understanding the Output:** Run the script `RSA2_c.py`
   - The program will display the generated prime numbers and private key.
   - finaly it will display the decrypted message.

[Sample Output]

```python
p: 27449
q: 27539
Public key: (e=163119273, n=755918011)
Private key: (d=528303353, n=755918011)
Decrypted message: [5342425, 564358176, 158153819, 140693186, 444627286, 515605488, 570912760, 444627286, 203238352, 743129578, 564968903, 594522526, 253138416, 681475929, 444752721, 743129578, 46261743, 539896832]
```
**observation:** 
- value of 'n' (755918011) is relatively small for RSA standards, but in practice, 'n' can be much larger, often hundreds of digits long. Similarly, the private key 'd' calculated using modular inverse can also be a large integer.
- public exponent 'e' (163119273) is larger,  but 'e' must be coprime with Euler's totient function of 'n' (phi(n)). 
- for efficiency and security reasons e is often chosen to be a fixed value:65537 

## 3. RSA and Coding
- This program encrypt a text (alphabet) by RSA. For this it is necessary to
transform the text into a number before encrypting it.

  - Open the script `RSA3_all.py`

This program consists of the following parts:
1. **Key pair generation**:
The program generates a private key/public key pair based on the specified key size (modulo n) in bits. It utilizes the RSA algorithm to generate large prime numbers and calculates the necessary parameters for the keys.
1. **Alphabet Encoding**:
The program uses a custom alphabet to encode and decode messages. The alphabet maps each character to a unique number, allowing text messages to be transformed into numbers for encryption and back into text after decryption.
1. **Block size calculation**:
Before encrypting a message, the program divides it into blocks. The block size is calculated based on the number of characters in the custom alphabet and the modulo n parameter of the RSA algorithm.
1. **Encryption**:
The program encrypts the message using the public key obtained from the key generation step. It breaks the message into blocks, converts each block into numbers using the custom alphabet encoding, and encrypts them using the RSA algorithm.
1. **Decryption**:
After encryption, the program decrypts the encrypted message using the private key obtained from the key generation step. It reverses the encryption process, decrypts each block using the RSA algorithm, and converts them back into text using the custom alphabet decoding.
1. **Binary Coding**:
The program can optionally encode the encrypted and decrypted messages into binary format. It converts the text messages into binary strings before encryption and after decryption, providing an alternative representation of the messages.

 **Understanding the Output:** Run the script `RSA3_all.py`
   - The program will display the generated public and private keys.
   - It will prompt you to enter a message to encrypt.
   - It will display the encrypted blocks and message
   - it will display the decrypted result  and 
   - It will ddisplay encrypted and decrypted messages in binary

[Sample Output]
```python
Public Key: (3355340719435110760090477864928288396623511456690977492503896531459708606941, 5101923890849165119379197522165371743416200691964339276350239007583979744553)
Private Key: (1366088011266390218777857293134357875484484011054822869061484077011872639481, 5101923890849165119379197522165371743416200691964339276350239007583979744553)
Enter your message: CRYPTO
Message as numbers: [2, 17, 24, 15, 19, 14]
Encrypted blocks: [818005781117560172845809432519852124590041937731584395959215777463731653642]
Encrypted message: QU1H??€_8YNVVPN?Y808RYP.RFVMBMC.S81ANR€AT4KHDVC
Decrypted numbers: [2, 17, 24, 15, 19, 14]
Decrypted message: CRYPTO
Encrypted message (binary): 010100010101010100110001010010000011111100111111111000101000001010101100010111110011100001011001010011100101011001010110010100000100111000111111010110010011100000110000001110000101001001011001010100000010111001010010010001100101011001001101010000100100110101000011001011100101001100111000001100010100000101001110010100101110001010000010101011000100000101010100001101000100101101001000010001000101011001000011
Decrypted message (binary): 010000110101001001011001010100000101010001001111
```
