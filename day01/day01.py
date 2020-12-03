import itertools

s = []

for i in range(0, 200):
    s.append(int(input()))

for i in range(0, 200):
    for j in range(i, 200):
        for k in range(j, 200):
            if s[i] + s[j] + s[k] == 2020:
                print(s[i] * s[j] * s[k])
                break
