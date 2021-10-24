from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gemstone, sculpture, gold, jewellery = 0, 0, 0, 0

while materials and magic_level:
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()
    total = current_material + current_magic_level

    if total < 100:
        if total % 2 == 0:
            total = current_material * 2 + current_magic_level * 3
        else:
            total = total * 2
    elif total > 499:
        total = total / 2

    if 100 <= total <= 199:
        gemstone += 1
    elif 200 <= total <= 299:
        sculpture += 1
    elif 300 <= total <= 399:
        gold += 1
    elif 400 <= total <= 499:
        jewellery += 1

if (gemstone >= 1 and sculpture >= 1) or (gold >= 1 and jewellery >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

if gemstone >= 1:
    print(f"Gemstone: {gemstone}")
if gold >= 1:
    print(f"Gold: {gold}")
if jewellery >= 1:
    print(f"Jewllwey: {jewellery}")
if sculpture >= 1:
    print(f"Porcelain Sculpture: {sculpture}")