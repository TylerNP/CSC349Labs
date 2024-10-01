import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()

found = False  
low = 0
high = len(lines)-1 
middle = high//2
count = 0
if high == -1:
    found = True
if middle == 0:
    print(lines[middle].strip())
    found = True

while not found:
    side_checked = 1
    adjustment = 0
    count += 1
    print(f"STEP {count}")
    #determine if middle is the first or second in the pair if it is not the singleton
    if middle % 2 == 0:
        side_checked = -1
        adjustment = 1

    value = int(lines[middle])
    if low >= high:
        found = True
        print(value)
        break
    if value == int(lines[middle-side_checked]):
        low = middle+1+adjustment
        middle = low+(high-low)//2
    elif value == int(lines[middle+side_checked]):
        high = middle-1-adjustment
        middle = low+(high-low)//2
    else:
        print(value)
        found = True
        
