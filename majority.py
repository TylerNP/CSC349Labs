import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = [line.strip() for line in file]

def majority(s_1 : list[int], s_2 : list[int]) -> list[int]:
    if not s_1:
        return s_2
    if not s_2:
        return s_1
    if s_1[-1] == s_2[-1]:
        s_1.append(s_2[-1])
        s_2.pop(0)
        return majority(s_1, s_2)
    else:
        if len(s_1) > len(s_2):
            return []
        else:
            return []

def majority_search(A : list[int]) -> list[int]:
    if not A:
        return []
    if len(A) == 1:
        print("RAN")
        return A
    middle = (len(A)-1)//2
    s_1 = majority_search(A[0 : middle : 1])
    s_2 = majority_search(A[middle+1 : len(A)-1 : 1])
    return majority(s_1, s_2)

print(majority_search(lines))
