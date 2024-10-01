import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()

def singleton_search(list, low, high):
    if low == high:
        return list[low]
    middle = low + (low-high)//2
    print(f"{low} {high} {middle}")
    if middle >= len(list):
        return 0
    if low >= high:
        return list[middle]
    adjustment = 0
    side_check = 1
    if (middle-low) % 2 == 0:
        adjustment = 1
        side_check = -1
    value = int(lines[middle])
    if value == int(lines[middle-side_check]):
        singleton_search(list, middle+1+adjustment, high)
    elif value == int(lines[middle+side_check]):
        singleton_search(list, low, middle-1-adjustment)
    else:
        return value

singleton_search(lines, 0, len(lines)-1)