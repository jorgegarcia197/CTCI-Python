

input_list = list(range(1, 1000))
factors = []

for i in input_list:
    if i % 3 == 0:
        factors.append(i)
    elif i % 5 == 0:
        factors.append(i)
    else:
        continue
print(sum(factors))
