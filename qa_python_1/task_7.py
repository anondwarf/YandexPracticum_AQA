def digital_root(num):
    if len(str(num)) == 1:
        return num

    sum = 0
    for i in str(num):
        sum += int(i)

    return digital_root(sum)

print(digital_root(4851))
print(digital_root(97569))
print(digital_root(889987))