#!/usr/bin/env python
# coding: utf-8

# # --- Day 4: The Ideal Stocking Stuffer ---
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
# 
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
# 
# For example:
# 
# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
# Your puzzle input is bgvyzdsv.


# Iterative method:
# Take input, add 1, convert to MD5, check 1st 5 digits, if not 00000, add 2, convert, check...

# Import the MD5 hashing function
import hashlib

# Define inputs to MD5
key = 'bgvyzdsv'
counter = 1

# Concatenate inputs (both must be strings)
concat = key + str(counter)

# Hash the concatenation into MD5 (must be encoded into unicode)
code = hashlib.md5(concat.encode('utf-8'))

# At any point you can ask it for the digest of the concatenation of the data fed to it so far using the digest() or hexdigest() methods.
# print(code.hexdigest())

# Iterate increasing the number until first 5 digits are 00000

while str(code.hexdigest())[0:5] != '00000':
    counter = counter + 1
    concat = key + str(counter)
    code = hashlib.md5(concat.encode('utf-8'))
    if counter%100000 == 0:
        print(counter)

print(code.hexdigest())
print(counter)


# # Part 2

# Now find one that starts with six zeroes.

# Check if first 6 digits are 000000
while str(code.hexdigest())[0:6] != '000000':
    counter = counter + 1
    concat = key + str(counter)
    code = hashlib.md5(concat.encode('utf-8'))
    
    # simple print to track progress every 100000 iterations
    if counter%100000 == 0:
        print(counter)

print(code.hexdigest())
print(counter)
