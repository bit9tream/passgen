#!/bin/env python3

import random
import argparse

charlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
            'q', 'Q', 'w', 'w', 'e', 'E', 'r', 'R', 't', 'T', 
            'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'a', 'A', 
            's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 
            'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X', 
            'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M']
passwd = ''


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lenght", type=int, action="store")
args = parser.parse_args()

if args.lenght == 0:
    l = int(input("Enter password lenght: "))
else:
    l = args.lenght


for num in range(0,l):
    passwd += str(random.choice(charlist))
print(passwd)
