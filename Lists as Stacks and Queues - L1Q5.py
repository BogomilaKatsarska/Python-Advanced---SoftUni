# OPTION I:
from queue import deque

children = deque(input().split())
count = int(input())


while len(children) > 1:
    children.rotate(-count)
    print(f"Removed {children.pop()}")

print(f"Last is {children.popleft()}")

# OPTION II:
# from collections import deque
# 
# potatoes = input().split(' ')
# potatoes_queue = deque(potatoes)
# step = int(input())
# 
# while potatoes_queue:
#     for _ in range(step-1):
#         potatoes_queue.append(potatoes_queue.popleft())
#     print(f'{potatoes_queue.popleft()} is out')
