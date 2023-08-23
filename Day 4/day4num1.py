import random
randoms = map(str, [random.randrange(0, 10) for i in range(10)])
with open("random.txt", "w") as f:
    for num in randoms: f.write(num + "\n")