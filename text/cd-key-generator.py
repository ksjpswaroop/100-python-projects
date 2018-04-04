'''
CD Key Generator
Generates a unique key for your applications to use based on some arbitrary algorithm that you can specify.
'''

import string
import secrets

def pass_gen():
    password = []
    alphabet = string.ascii_uppercase + string.digits
    for i in range(8):
        psw = ''.join(secrets.choice(alphabet) for i in range(5))
        password.append(psw)
    password = '-'.join(password)
    return password

print(pass_gen())
