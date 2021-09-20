n = int(input())
stack = []

for i in range(n):
    command = input().split()
    if command[0] == '1' :
        stack.append(command[1])
    if command[0] == '2':
        if stack:
            stack.pop()
    if command[0] == '3':
        if stack:
            print(max(stack))
    if command[0] == '4':
        if stack:
            print(min(stack))

reversed_nums = []
for i in range(len(stack)):
    reversed_nums.append(str(stack.pop()))
print(', '.join(reversed_nums))


