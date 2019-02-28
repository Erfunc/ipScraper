#!usr/bin/env python3

import re

# ValidIpAddressRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
ValidIpAddressRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\w*";

ipsFound = []
pattern = re.compile(ValidIpAddressRegex)

try:
    with open ('inputFile.txt', 'rt') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) != None:
                ipsFound = re.search(pattern, line)
            # print(ipsFound, file=open("extractedIP's.txt", "a"))
                print(ipsFound.group(), file=open("extractedIP's.txt", "a"))
                print(ipsFound.group())


except FileNotFoundError:
    print("Log file not found.")

