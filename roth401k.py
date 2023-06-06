

n = 22500
r = 0.07

y = 10  # number of years

total = 0
for i in range(y):
    print(" year ", i)
    print(" total ", total)
    total += (total + n) * (1 + r)
