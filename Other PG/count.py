import sys

filename = sys.argv[-1]
with open(filename, 'r') as file:
    lines = file.readlines()

unique = []
uniqueCount = []
sum = 0
for line in lines:
    sum += 1
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

write = open("output.txt", 'w')
i = 0
for cnt in uniqueCount:
    print(f"{unique[i].strip()}: {cnt} rf: {cnt/sum}\n")
    i += 1

print(f"\nSum: {sum}")
