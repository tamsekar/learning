# put your python code here
m1_1 = int(input())
m1_2 = int(input())
m1_3 = int(input())
m2_1 = int(input())
m2_2 = int(input())
m2_3 = int(input())

# Time conversion
m1_1_total_secs = m1_1 * 60 * 60
m1_2_total_secs = m1_2 * 60
m1_3_total_secs = m1_3 * 1
m2_1_total_secs = m2_1 * 60 * 60
m2_2_total_secs = m2_2 * 60
m2_3_total_secs = m2_3 * 1

m1_total_secs = (m1_1_total_secs + m1_2_total_secs + m1_3_total_secs)
m2_total_secs = (m2_1_total_secs + m2_2_total_secs + m2_3_total_secs)

print(abs(m1_total_secs - m2_total_secs))