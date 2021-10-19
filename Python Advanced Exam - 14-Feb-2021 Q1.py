effects = [int(x) for x in input().split(", ")[::-1]]
power = [int(x)for x in input().split(", ")]

palm = 0
willow = 0
crossette = 0

end_flag = False
win_flag = False
while True:
    if effects == [] or power == []:
        end_flag = True
        break

    while effects[-1] <= 0:
        effects.pop()
        if effects == []:
            end_flag = True
            break

    while power[-1] <= 0:
        power.pop()
        if power == []:
            end_flag = True
            break

    if end_flag:
        break

    current_effect = effects[-1]
    current_power = power[-1]

    if (current_power + current_effect) % 3 == 0 and not (current_power + current_effect) % 5 == 0:
        palm += 1
        effects.pop()
        power.pop()
    elif (current_power + current_effect) % 5 == 0 and not (current_power + current_effect) % 3 == 0:
        willow +=1
        effects.pop()
        power.pop()
    elif (current_power + current_effect) % 5 == 0 and (current_power + current_effect) % 3 == 0:
        crossette +=1
        effects.pop()
        power.pop()
    else:
        current_effect -= 1
        effects.pop()
        effects.insert(0, current_effect)

    if palm == 3 and willow == 3 and crossette == 3:
        win_flag = True
        break

if end_flag:
    print("Sorry. You can't make the perfect firework show.")
elif win_flag:
    print("Congrats! You made the perfect firework show!")

if effects:
    ef_str = map(str, effects[::-1])
    print(f"Firework Effects left: {', '.join(ef_str)}")

if power:
    pow_str = map(str, power)
    print(f"Explosive Power left: {', '.join(pow_str)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")