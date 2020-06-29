# Code
a = int(input())
y = 0

while a < 700000:
    a = a + (a) * 0.071
    y += 1
print(y)
