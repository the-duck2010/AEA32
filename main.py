#!/bin/python

from random import randint
import argparse

parser = argparse.ArgumentParser(prog="AEA32", description="A simple python CLI / library for 32-bit encryption")
parser.add_argument("-e", "--encrypt", help="Encrypt the following text")
parser.add_argument("-d", "--decrypt", help="Decrypt the following text")
parser.add_argument("-k", "--key", help="The key used for operations")
parser.add_argument("--keygen", help="Generate a 32-bit encryption key", action="store_true", default=False)
args = parser.parse_args()

class aea32(): 

    def keygen():
        key = str(randint(0, 4))
        for _ in range(31):
            key = key + str(randint(0, 4))
        return key

    def encrypt(key = keygen(), text = ""):
        nkey = key
        ntext = ""
        klen = len(nkey)
        tlen = len(text)
        while tlen > klen:
            nkey = nkey + key
            klen = len(nkey)
        ntext = ''.join(chr(ord(text[char]) + int(nkey[char])) for char in range(tlen))
        return ntext

    def decrypt(key = keygen(), text = ""):
        nkey = key
        ntext = ""
        klen = len(nkey)
        tlen = len(text)
        while tlen > klen:
            nkey = nkey + key
            klen = len(nkey)
        ntext = ''.join(chr(ord(text[char]) - int(nkey[char])) for char in range(tlen))
        return ntext
    
if __name__ == "__main__":
    parser.print_help()
    exit()

if not args.key and not args.keygen:
    print("AEA32: error: argument -k expected but not found")
    exit()

if args.keygen:
    print("32-bit key successfully generated!")
    print("--------------------------------")
    print(aea32.keygen())
    print("--------------------------------")
    exit()

if args.encrypt and args.key:
    print(aea32.encrypt(args.key, args.encrypt))

if args.decrypt and args.key:
    print(aea32.decrypt(args.key, args.decrypt))
