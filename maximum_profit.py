N = input()
R_min = input()
R_max = 0
diff_max = R_max - R_min

R = R_min
for i in range(0, N-1):
    R = input()
    a = R - R_min
    if diff_max < a:
        diff_max = a
    if R < R_min:
        R_min = R

print(diff_max)