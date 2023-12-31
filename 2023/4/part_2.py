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

def get_copies(card_id):
    copies = 0
    winning, ours = get_nums(card_id)
    for our in ours:
        if our in winning:
            copies += 1
    s[0]+=1
    if cards.get(card_id):
        cards[card_id] += 1
    else:
        cards[card_id] = 1
    for copy in range(card_id+1, card_id+copies+1):
        # print(copy)
        get_copies(copy)
    #     s_card_points+=get_points(copy)
    # return s_card_points

def get_nums(card_id):
    line = r[card_id-1]
    line = line[10:]
    winning, ours = line.split(" | ")
    winning = list(map(lambda x: int(x), filter(lambda x: x.strip()!='', winning.split(" "))))
    ours = list(map(lambda x: int(x), filter(lambda x: x.strip()!='', ours.split(" "))))
    return winning, ours

s = [0,]
cards = {}
for i,line in enumerate(r):
    i+=1
    get_copies(i)
    # s += get_copies(i)

print("Result is: ", s[0])
print(cards)