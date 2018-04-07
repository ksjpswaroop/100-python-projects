'''
Vigenere / Vernam / Ceasar Ciphers - Functions for encrypting and decrypting data messages. Then send them to a friend.
'''
import string
from itertools import cycle
import functools

alphabet = string.ascii_lowercase


def vigenere(text, keyword):
    pairs = zip(text, cycle(keyword))
    cipher = ""

    for pair in pairs:
        total = functools.reduce(lambda x, y: alphabet.index(x) + alphabet.index(y), pair)
        cipher += alphabet[total % 26]

    return cipher


def decrypt_vigenere(cipher, keyword):
    pairs = zip(cipher, cycle(keyword))
    result = ""

    for pair in pairs:
        total = functools.reduce(lambda x, y: alphabet.index(x) - alphabet.index(y), pair)
        result += alphabet[total % 26]

    return result


def vernam(text, key):
    result = ""
    pointer = 0

    for char in text:
        result += chr(ord(char) ^ ord(key[pointer]))
        pointer += 1
        if pointer == len(key):
            pointer = 0

    return result


def ceasar(text, key):
    result = ""

    for l in text.lower():
        try:
            i = (alphabet.index(l) + key) % 26
            result += alphabet[i]
        except ValueError:
            result += l

    return result


def decrypt_ceasar(text, key):
    result = ""

    for l in text:
        try:
            i = (alphabet.index(l) - key) % 26
            result += alphabet[i]
        except ValueError:
            result += l

    return result


#command line

choice = input("1.Vigenere\n2.Vernam\n3.Ceasar\n")

if choice == "1":
    choice = input("1.Encrypt\n2.Decrypt\n")

    if choice == "1":
        text = input("Text: ")
        keyword = input("Keyword: ")
        print(vigenere(text.lower(), keyword.lower()))

    elif choice == "2":
        cipher = input("Cipher: ")
        key = input("Keyword: ")
        print(decrypt_vigenere(cipher.lower(), key.lower()))

    else:
        print('Error input')

elif choice == "2":
    choice = input("1.Encrypt\n2.Decrypt\n")

    if choice == "1":
        text = input("Text: ")
        key = input("Key: ")
        print(vernam(text, key))

    elif choice == "2":
        cipher = input("Cipher: ")
        key = input("Key: ")
        print(vernam(cipher, key))

    else:
        print('Error input')

elif choice == "3":
    choice = input("1.Encrypt\n2.Decrypt\n")

    if choice == "1":
        text = input("Text: ")
        key = input("Key: ")
        print(ceasar(text, int(key)))

    elif choice == "2":
        cipher = input("Cipher: ")
        key = input("Keyword: ")
        print(decrypt_ceasar(cipher.lower(), int(key)))

    else:
        print('Error input')

else:
    print('Error input')
