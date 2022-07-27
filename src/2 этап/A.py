B = []

he = []
en = []

with open("./input.txt", "r") as file:
    line = file.readline()
    while line:
        line = line.split("(")
        line[1] = line[1].split(",")
        line[1][1] = line[1][1][:-2]
        line[1][0], line[1][1] = int(line[1][0]), int(line[1][1])
        B.append(line)
        line = file.readline()

i = len(B) - 1

while B[i][0] != "Init":
    i -= 1

en.append(B[i][1][0])
en.append(B[i][1][1])


def get_va(index):
    if index >= len(he):
        index -= len(he)
        return en[index]
    else:
        return he[-index - 1]


i += 1

while i < len(B):
    if B[i][0] == "NewTail":
        en.append(get_va(B[i][1][0]) + get_va(B[i][1][1]))
    else:
        he.append(get_va(B[i][1][0]) + get_va(B[i][1][1]))
    i += 1

he = list(map(str, he))
en = list(map(str, en))
he.reverse()
print(" ".join(he), " ".join(en))