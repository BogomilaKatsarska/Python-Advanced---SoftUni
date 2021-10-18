jobs = [int(x) for x in input().split(", ")]
index = int(input())
total_cycles = 0
for x in jobs:
    if x <= jobs[index]:
        total_cycles += x
print(total_cycles)