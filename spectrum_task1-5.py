v1 = {1,2,3,4,5,6,7,8,9}
v2 = {1,3,4,6,8,11,22,34,51,67}

for i in list(v1):
    for j in list(v2):
        if i==j:
            v1.remove(i)
            l = set(v1)

print(l)
