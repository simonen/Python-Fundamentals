line1 = input()
line2 = input()
line3 = input()

A = line1.split()
B = line2.split()
C = line3.split()

p1_win = False
p2_win = False
winner = ''

for index0 in range(0, 3):
    for index1 in range(0, 3):
        for index2 in range(0, 3):
            if (index0 == index1 == index2) or (index0 == 0 and index1 == 1 and index2 == 2) or \
                    (index0 == 2 and index1 == 1 and index2 == 0):
                pass
            else:
                continue
            if (A[index0] == "1" and B[index1] == "1" and C[index2] == "1") or \
                    (A.count("1") == 3 or B.count("1") == 3 or C.count("1") == 3):
                p1_win = True
                winner = 'First'
                break
            elif (A[index0] == "2" and B[index1] == "2" and C[index2] == "2") or \
                    (A.count("2") == 3 or B.count("2") == 3 or C.count("2") == 3):
                p2_win = True
                winner = 'Second'
                break
        if p1_win or p2_win:
            break
    if p1_win or p2_win:
        print(f"{winner} player won")
        break
else:
    print("Draw!")
