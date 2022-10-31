def increase_river(num):
    if 1 <= num <= 9:
        return num * 2
    separated_num = [int(n) for n in str(num)]
    for i in range(len(separated_num)):
        num += separated_num[i]
    return num


# print(increase_river(14))
r1 = 32
r2 = 47

while r1 != r2:
    if r1 < r2:
        r1 = increase_river(r1)
    else:
        r2 = increase_river(r2)

