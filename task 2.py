c1 = 10
b1 = 4
t = 0
b = 0
while True:
    if c1 > 0:
        c1 -= 1
        t += 2
        b += 1
    if b//b1 == 1:
        c1 += 1
        b = 0
    if c1 == 0 and b < b1:
        break
print(t)


