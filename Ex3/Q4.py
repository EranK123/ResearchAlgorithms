vals = [3, 2, 4, 2,1,5]
worst_diff = 0
for i in range(len(vals)):
    if worst_diff < vals[i]:
        for j in range(i + 1, len(vals)):
            t = vals[i] - vals[j]
            worst_diff = max(t, worst_diff)
print(-worst_diff)

