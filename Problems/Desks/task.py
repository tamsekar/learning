class_a = abs(int(input()))
class_b = abs(int(input()))
class_c = abs(int(input()))

desk_a = ((class_a // 2) + (class_a % 2))
desk_b = ((class_b // 2) + (class_b % 2))
desk_c = ((class_c // 2) + (class_c % 2))

print(desk_a + desk_b + desk_c)
