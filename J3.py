people = int(input())
lines = []

for i in range(people):
    line = input()
    lines.append(line)

counts = []

for i in range(5):
    count = 0
    for line in lines:
        if line[i] == 'Y':
            count += 1
    counts.append(count)

max_val = max(counts)
output = ''



for i in range(len(counts)):
    if counts[i] == max_val:
        output = output + str(i+1) + ','

print(output[0:-1])
