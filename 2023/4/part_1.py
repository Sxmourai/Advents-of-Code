import sys
file_name = "input"
if len(sys.argv)>1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.readlines()
s = 0
for line in r:
    card_points = 0
    line = line[10:]
    print(line)
    winning, ours = line.split(" | ")
    winning = list(map(lambda x: int(x), filter(lambda x: x.strip()!='', winning.split(" "))))
    ours = list(map(lambda x: int(x), filter(lambda x: x.strip()!='', ours.split(" "))))
    # print(winning, ours)
    for our in ours:
        if our in winning:
            if card_points == 0:
                card_points=1
            else:
                card_points *= 2
    print(card_points)
    s+=card_points

print("Result is: ", s)