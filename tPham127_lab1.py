import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()

def singleton_search(list : list[int], low : int, high : int) -> None:
    if low == high:
        print(list[low].strip())
        return None
    middle = low + (high-low)//2
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
        print(value)

singleton_search(lines, 0, len(lines)-1)