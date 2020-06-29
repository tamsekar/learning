# put your python code here
rect_a = int(input())
rect_b = int(input())
rect_c = int(input())

sum_edges = 4 * (rect_a + rect_b + rect_c)
surface_area = 2 * ((rect_a * rect_b) + (rect_b * rect_c) + (rect_c * rect_a))
volume_ = (rect_a * rect_b * rect_c)

print(sum_edges)
print(surface_area)
print(volume_)
