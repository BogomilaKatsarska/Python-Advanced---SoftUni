n, m = [int(x) for x in input().split()]
first = set()
second = set()

for _ in range(n):
    first.add(input())
for _ in range(m):
    second.add(input())

result = first.intersection(second)
for el in result:
    print(el)