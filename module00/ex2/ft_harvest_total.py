def ft_harvest_total():
    total = 0
    for i in range(1, 4):
        total += int(input(F"Day {i} harvest: "))
    print(F"Total harvest: {total}")
