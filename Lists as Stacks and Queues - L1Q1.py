n = list(input())
reversed_stack = []

while n:
    a =n.pop()
    reversed_stack.append(a)

print(f"{''.join(reversed_stack)}")