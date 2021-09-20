input = list(input().split())
stack = []

while input:
    last_el = input.pop()
    stack.append(last_el)
print(f"{' '.join(stack)}")