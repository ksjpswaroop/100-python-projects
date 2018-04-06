'''
Vigenere Cipher - Functions for encrypting and decrypting data messages. Then send them to a friend.
'''
import string
from itertools import cycle
import functools

alphabet = string.ascii_lowercase


def vigenere(text, keyword):
    pairs = zip(text, cycle(keyword))
    cipher = ''

    for pair in pairs:
        total = functools.reduce(lambda x, y: alphabet.index(x) + alphabet.index(y), pair)
        cipher += alphabet[total % 26]

    return cipher.lower()


def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    plaintext = ''

    for pair in pairs:
        total = functools.reduce(lambda x, y: alphabet.index(x) - alphabet.index(y), pair)
        plaintext += alphabet[total % 26]

    return plaintext


text = input("Text: ")
keyword = input("Keyword: ")
print(vigenere(text.lower(), keyword.lower()))

cipher = input("Cipher: ")
key = input("Keyword: ")
print(decrypt(key.lower(), cipher.lower()))
