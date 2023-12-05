import sys
file_name = "input"
if len(sys.argv)>1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.readlines()

def get_points(card_id):
    points = 0
    winning,ours = get_nums(card_id)
    for our in ours:
        if our in winning:
            points += 1
    return points

def get_nums(card_id):
    line = r[card_id-1]
    line = line[8:]
    winning, ours = line.split(" | ")
    winning = list(map(lambda x: int(x), filter(lambda x: x.strip()!='', winning.split(" "))))
    ours = list(map(lambda x: int(x), filter(lambda x: x.strip()!='', ours.split(" "))))
    return winning, ours

def get_copies(card_id):
    copies = 0
    winning, ours = get_nums(card_id)
    for our in ours:
        if our in winning:
            copies += 1
    s_card_points = 1
    for copy in range(card_id+1, card_id+copies):
        s_card_points+=get_copies(copy)
    if card_id == 1:
        print(card_id, s_card_points, copies)
        
        print(s_card_points)
    return s_card_points

s = 0
for i,line in enumerate(r):
    i+=1
    # print(s)
    copies = get_copies(i)
    # print(i,copies)
    s += copies

print("Result is: ", s)