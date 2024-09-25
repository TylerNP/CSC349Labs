import sys

if len(sys.argv) != 2:
    print("ERROR: Include a filename")
    exit()
filename = sys.argv[1]
try:
    file = open(filename, 'r')
except:
    print("ERROR: File ({}) not found in directory".format(filename))
    exit()
lines = file.readlines()

found = False  
low = 0
high = len(lines)-1 
middle = high//2

if high == -1:
    print("ERROR: Empty list")
    exit()

if middle == 0:
    print(lines[middle].strip())
    found = True

while not found:

    value = int(lines[middle])
    if value == int(lines[middle-1]):
        low = middle+1
        middle = low-1+(high-low)//2
    elif value == int(lines[middle+1]):
        high = middle-1
        middle = low+1+(high-low)//2
    else:
        print(value)
        found = True
