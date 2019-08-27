#!/usr/bin/python3
# удаляет пустые строки и номера строк
import sys
import re

if len(sys.argv) != 2:
    print('need 2 arguments')
    exit()

file1 = sys.argv[1]
file2 = 'new_' + file1

with open(file1, 'r') as f1, open(file2, 'w') as f2:
    for line in f1:
        if line.isspace():
            continue
        else:
            new_line = re.sub(r'\w+:', '', line)
            f2.write(new_line)



