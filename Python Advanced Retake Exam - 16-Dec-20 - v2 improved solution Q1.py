from collections import deque

males, females = deque([int(x) for x in input().split()]), deque([int(x) for x in input().split()])
matches_counter = 0

while males and females:
    current_male = males.pop()
    if current_male <= 0:
        continue

    current_female = females.popleft()
    if current_female <= 0:
        males.append(current_male)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue

    if current_female == current_male:
        matches_counter += 1
    else:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches_counter}")
if males:
    print(f"Males left: {', '.join([str(x) for x in list(males)[::-1]])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")