import random

data = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = random.randint(1, 100)

for row in data:
    print(row)
