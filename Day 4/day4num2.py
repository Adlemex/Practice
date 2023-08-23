with open("random.txt", "r") as f:
    data = f.read()
with open("copy_of_random.txt", "w") as f:
    f.write(data)

replacements = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
                6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
with open("copy_of_random.txt", "r+") as f:
    data = f.readlines()
    f.seek(0)
    f.flush()
    res = []
    for line in data:
        res.append(str(replacements.get(int(line.replace("\n", "")))) + "\n")
    print(res)
    f.writelines(res)