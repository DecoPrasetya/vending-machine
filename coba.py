xu = []

for i in range(5):
    yu = []
    for j in range(5):
        if i < j:
            yu.append(j)
        else:
            yu.append(0)
    xu.append(yu)
print(xu)

