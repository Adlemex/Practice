#1
def sum_list_elems(l: list[int, float]) -> float:
    res = float(0)
    for elem in l:
        res += float(elem)
    return res

#2
def write_reverse(string: str):
    with open("reversed_string.txt", "w") as f:
        f.write(string[::-1] + "\n")
