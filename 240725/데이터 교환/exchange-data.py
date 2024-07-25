a, b, c = 5, 6, 7
tmp1 = b
b = a
tmp2 = c
c = tmp1
a = tmp2
print(f"{a}\n{b}\n{c}")