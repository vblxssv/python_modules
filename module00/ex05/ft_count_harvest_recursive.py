

def ft_rec(rem):
    if rem != 0:
        ft_rec(rem - 1)
        print(F"Day {rem}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_rec(days)
    print("Harvest time!")
