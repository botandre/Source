import string

# Make a dict of lower and uppercase letters with enumeration
LOW2I = dict(zip(string.ascii_lowercase, range(26)))
I2LOW = dict(zip(range(26), string.ascii_lowercase))

UPP2I = dict(zip(string.ascii_uppercase, range(26)))
I2UPP = dict(zip(range(26), string.ascii_uppercase))

message = input("Message: ")
key = int(input("Key: "))

def encrypt(message, key):
    ciphertext = ""
    for c in message:
        if c.isalpha():
            if c.islower():
                ciphertext += I2LOW[ (LOW2I[ c ] + key) % 26 ]
            elif c.isupper():
                ciphertext += I2UPP[ (UPP2I[ c ]  + key) % 26 ]
        else:
            ciphertext += c

    return ciphertext

encrypted_message = encrypt(message, key)
print(encrypted_message)
