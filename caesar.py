import string
import sys

def args():
    if (len(sys.argv) < 3):
        print("Usage: {} 'message' key".format(sys.argv[0]))
        print("Usage: {} '-b' message max_range".format(sys.argv[0]))
        sys.exit(1)

    if (("-b" in sys.argv[1]) or ("--brute" in sys.argv[1])):
        del sys.argv[1]

        return 1

    return 0

lower2i = dict(zip(string.ascii_lowercase, range(26)))
i2lower = dict(zip(range(26), string.ascii_lowercase))

upper2i = dict(zip(string.ascii_uppercase, range(26)))
i2upper = dict(zip(range(26), string.ascii_uppercase))

def encrypt(message, key):
    ciphertext = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                ciphertext += i2lower[ (lower2i[ char ] + key) % 26 ]
            else:
                ciphertext += i2upper[ (upper2i[ char ]  + key) % 26 ]
        else:
            ciphertext += char

    return ciphertext

def decrypt(message, key):
    deciphertext = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                deciphertext += i2lower[ (lower2i[ char ] - key) % 26 ]
            else:
                deciphertext += i2upper[ (upper2i[ char ]  - key) % 26 ]
        else:
            deciphertext += char

    return deciphertext


def bruteForce(encoded, _range):
    for key in range(1, _range):
        brute = decrypt(encoded, key)
        _print(brute, key)


def _print(message, key):
    print("[+] Key {} = {}".format(key, message))

def main():
    brute = args()
    
    message = sys.argv[1]
    key = int(sys.argv[2])

    if(brute):
        bruteForce(message, key)
    else:
        encoded = encrypt(message, key)
        decoded = decrypt(encoded, key)

        print("[+] Original string: {}".format(message))
        print("[+] Encoded string with key {}: {}".format(key, encoded))
        print("[+] Decoded string with key {}: {}".format(key, decoded))


if __name__ == "__main__":
    main()