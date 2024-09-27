import sys
import math

filename = sys.argv[-1]
with open(filename, 'r') as file:
    lines = file.readlines()

unique = []
uniqueCount = []
sum = 0
sumValue = 0
lines.sort()
for line in lines:
    sum += 1
    sumValue += int(line.strip())
    if len(unique) == 0:
        unique.append(line.strip())
        uniqueCount.append(1)
    else:
        count = 0
        found = False
        for elm in unique:
            if line.strip() == elm:
                found = True
                uniqueCount[count] += 1

            count += 1
        if not found:
            unique.append(line.strip())
            uniqueCount.append(1)

i = 0
for cnt in uniqueCount:
    print(f"{unique[i].strip()}: {cnt} rf: {cnt/sum}")
    i += 1

print(f"\nSum: {sum} Avg: {sumValue/sum}")
if sum % 2 == 0:
    print(f"Median: {(list[sum//2]+list[sum//2+1])/2})")
else:
    print(f"Median: {lines[sum//2]}")
max = -1
index = -1
for i in range(len(unique)):
    if uniqueCount[i] > max:
        max = i
        index = i
mode = unique[index]
print(f"Mode: {unique[index]}")

variance = 0
for i in range(len(unique)):
    mean = sumValue/sum
    temp = round(float(unique[i])-mean, 2)
    squared = round(temp*temp, 2)
    variance += squared * uniqueCount[i]
    print(f"{unique[i]} | {mean} | {temp} | {squared}")
print(f"{variance}, {variance/len(unique)}")
print(math.sqrt(variance/len(unique)))