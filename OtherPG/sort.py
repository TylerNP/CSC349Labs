import sys

filename = sys.argv[-1]
with open(filename, 'r') as file:
    lines = file.readlines()

lines.sort()
file.close()


with open(filename, 'w') as writeFile:
    for line in lines:
        writeFile.write(line.strip() + "\n")