base_a = input()
base = base_a.split()
base[0] = int(base[0])
base[1] = int(base[1])
score = []
attend = []
for n in range(base[0]):
    data = input()
    tmp = data.split()
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    score.append(tmp[0])
    attend.append(tmp[1])

for a in range(base[0]):
    ans = score[a] - attend[a] * 5

    if ans >= base[1]:
        print(a + 1)
    elif base[1] == 0:
        print(a + 1)




