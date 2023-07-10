# From https://www.youtube.com/watch?v=vsLBErLWBhA
# ----------------------------
# run with $ python3 encrypt.py
# A routine for python3
# Composed in IDLE (3.6.9) IDE
# Author: Mitch Bayliss
# E-mail: mitch@ur3.uk
# Date: 9 Jul 2023
# Licence: Creative Commons (CC)
#-------------------------------

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alpha = list(alpha)
# random.shuffle(alpha)
# print(alpha)
# LFUWGHXBOAYKEITPMDVNCJQZSR

#ENCRYPT
# The user, types in a plain-text message.
plain_text = input("Enter a message to encrypt: ")

# This is where the cipher-text will be held.
cipher_text = ""

# loop for (every instance) each letter and space, in the message.
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]     # append the latest letter to the cipher-string

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")
