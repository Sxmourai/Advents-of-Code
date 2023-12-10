import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.read()

strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]
def get_strength(letter):
    return strengths.index(letter)


all_cards = {}

for i,line in enumerate(r.splitlines(keepends=False)):
    card,bid = line.split(" ")
    occu = {}
    card_type = 0
    for letter in card:
        occu[letter] = occu.get(letter, 0)+1
    occu = sorted(occu.items(), key=lambda item: item[1], reverse=True)
    
    
    s = sorted(card)
    if len(set(s)) == 1:
        card_type = 7
    elif s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        card_type = 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        card_type = 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        card_type = 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        card_type = 3
    elif len(set(s)) == 4:
        card_type = 2
    elif len(set(s)) == 5:
        card_type = 1
    # if occu[0][1] == 5:
    #     card_type = 6
    # elif occu[0][1] == 4:
    #     card_type = 5
    # elif occu[0][1] == 3 and occu[1][1]==2:
    #     card_type = 4
    # elif occu[0][1] == 3:
    #     card_type = 3
    # elif occu[0][1] == 2 and occu[1][1]==2:
    #     card_type = 2
    # elif occu[0][1] == 2:
    #     card_type = 1
    # elif occu[0][1] == 1:
    #     if len(occu)!=5:
    #         print(occu)
    #     card_type = 0
    # else:
    #     print("ERROR", occu, card, bid,i)
    
    all_cards[card_type] = all_cards.get(card_type, []) + [((card,bid)),]
all_cards = dict(sorted(all_cards.items(), key=lambda card: card[0]))
print(all_cards)
ranks = []
for type,cards in all_cards.items():
    if len(cards)>1:
        for card in reversed(sorted(cards, key=lambda x: "".join([str(get_strength(letter)) for letter in x[0]]))):
            ranks.append(card[1])
        # for i in range(5):
        #     max_strength = ["22222",] # Least priority
            # for current_card in cards:
            #     print(current_card, max_strength)
            #     if get_strength(current_card[0][i])>get_strength(max_strength[0][i]):
            #         if max_strength[0]!="22222":
            #             cards.remove(current_card)
            #             ranks.append(current_card[1]) # Append bid
            #         else:
            #             max_strength=current_card
    else:
        ranks.append(cards[0][1])
s = 0
for i,bid in enumerate(ranks):
    # print(int(bid)*(i+1), i,bid)
    s += int(bid)*(i+1)
print(s)
